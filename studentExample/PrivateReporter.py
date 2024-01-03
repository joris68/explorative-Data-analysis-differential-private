from math import floor
import pydp as dp
import pandas as pd
from pydp.algorithms.laplacian import BoundedMean,Count #BoundedMedian, Count
import statistics as s
import numpy as np
import math


class PrivateReporter:

     def __init__(self, epsilon: float):
          self.dataFrame = pd.read_csv("student_grades.csv")
          #epsilon is the privacy budget here
          self.epsilon = epsilon 

     def calc_private_mean(self)-> float:
          # min Points 0 , max Points 100
          x = BoundedMean(self.epsilon,  dtype="float", lower_bound=0, upper_bound=100)
          return x.quick_result(list(self.dataFrame["Grade"]))

     #def calc_private_median(self)-> float:
      #    x = BoundedMedian(self.epsilon,  dtype="float")
       #   return x.quick_result(list(self.dataFrame["Grade"]))


     def calc_private_students_failed(self, threshold:int) -> int:
          x = Count(self.epsilon , dtype="float")
          #return x.quick_result(list(self.dataFrame[self.dataFrame["Grade"] < threshold ]))
          return x.quick_result(list(self.dataFrame[self.dataFrame["Grade"] < threshold ]['Grade']))
     
     def calc_private_students_passed(self, threshold:int) -> int:
          x = Count(self.epsilon , dtype="float")
          #return x.quick_result(list(self.dataFrame[self.dataFrame["Grade"] < threshold ]))
          return x.quick_result(list(self.dataFrame[self.dataFrame["Grade"] < threshold ]['Grade']))
     
     def bin_private_grades(self, bin_size: int):
          a = floor(100 / bin_size)
          # mehr bins brauchen wir wirklich nicht
          bins = [a *x for x in range(0,15) if a*x <= 100]
          self.dataFrame['bins'] = pd.cut(self.dataFrame['Grade'], bins=bins)
          #print("this is the dataframe head:")
          #print(self.dataFrame.head())
          #----------------------------
          frequencies, bins_a = np.histogram(self.dataFrame['Grade'], bins=bins)

          #print("Bins: " + str(bins_a))
          #print("Frequencies: " + str(frequencies))
          data_array = np.array(frequencies)

          # Reshape the array into a list of lists
          list_of_lists = data_array.reshape(-1, 1).tolist()

          #print(str(list_of_lists))



          #b = self.dataFrame.groupby('bins').apply(list)

          #print("This is B: " )
          ##print(b)


          private_grade_bin = []
          #data_lists = list(b)

         # print("this is data_lists: " +  str(data_lists))
          for data in list_of_lists:
               x = Count(1.82)
               count = x.quick_result(data)  # accepts only list as input
               
               private_grade_bin.append(count)
          
          #print("Type frqunecies" +  str(type(frequencies)))
          #print("Lenght frequency:" + str(len(frequencies)) )
          #print("Lenght privats:" + str(len(private_grade_bin)))
          new_frequencies = frequencies.tolist()
          list_to_return = []
          for x in range(0,len(new_frequencies)):
               list_to_return.append(private_grade_bin[x] + new_frequencies[x]) 
          return list_to_return
          
     def private_2(self, bin_size):
          a = floor(100 / bin_size)
          # mehr bins brauchen wir wirklich nicht
          bins = [a *x for x in range(0,15) if a*x <= 100]
          self.dataFrame['bins'] = pd.cut(self.dataFrame['Grade'], bins=bins)
          print("this is the dataframe head:")
          print(self.dataFrame.head())
          #----------------------------
          frequencies, bins_a = np.histogram(self.dataFrame['Grade'], bins=bins)

          print("Bins: " + str(bins_a))
          print("Frequencies: " + str(frequencies))

          private_list = []
          for bin in bins:
               x = Count(1.82 , dtype="float")
               a= x.quick_result(list(self.dataFrame[self.dataFrame == bin ]["bins"]))
               private_list.append(a)
          
          return private_list

# E - differential Private if Laplace(1/ epsilon) epsilon ist das privacy budget? 


     

if __name__ == "__main__":

     pr = PrivateReporter(0.9)
     a = pr.bin_private_grades(10)

     print("This is the private list: " + str(a))

     





