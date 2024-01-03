# this handler does not support the differencial Privacy
from math import floor
import pandas as pd
import statistics as s

class Reporter:

     def __init__(self):
          self.dataFrame = pd.read_csv("student_grades.csv")

     def calc_mean(self)-> float:
          return s.mean(list(self.dataFrame["Grade"]))

     def calc_median(self)-> float:
          return s.median(list(self.dataFrame["Grade"]))
     
     def calc_students_failed(self, threshold: int) -> int:
          return len(self.dataFrame[self.dataFrame['Grade'] < threshold])
     
     def calc_students_passed(self, threshold: int) -> int:
          return len(self.dataFrame[self.dataFrame['Grade'] >= threshold])
     
     # bins data 
     def bin_grades(self, bin_size) -> list[int]:
          a = floor(100 / bin_size)
          # mehr bins brauchen wir wirklich nicht
          bins = [a *x for x in range(0,15) if a*x <= 100]
          binned_values = pd.cut(self.dataFrame['Grade'], bins=bins)
          bin_counts = binned_values.value_counts().sort_index()
          return bin_counts.tolist()



     
          
if __name__ == "__main__":
     r = Reporter()
     print(r.calc_students_failed(50))
     #print(r.calc_mean())
     #print(r.calc_median())
     #a= 10
     #bins = [a *x for x in range(0,15) if a*x <= 100]
     #print(bins)
     #data = pd.read_csv("student_grades.csv")
     #bins =[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
     #binned_values = pd.cut(data['Grade'], bins=bins)
     #a =binned_values.value_counts().sort_index()
    # b = a.to_list()
     #print(b)
