from Reporter import Reporter
from PrivateReporter import PrivateReporter
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

     # reporter Objekte erstellen
     rep = Reporter()

     # mit verschiedenen Privacy Budgets
     pr_1 = PrivateReporter(0.4)
     pr_2 = PrivateReporter(0.7)

     list_normal = rep.bin_grades(10)
     priv_list1 = pr_1.bin_private_grades(10)
     priv_list2 = pr_2.bin_private_grades(10)
     
     
     print("These are the binnes values:")

     print(str(list_normal))
     print(priv_list1)
     print(priv_list2)

     print("These are the averages")
     print("Normal " + str(rep.calc_mean()))
     print("Epsilon 0.4: " + str(pr_1.calc_private_mean()))
     print("Epsilon 0.7: " + str(pr_2.calc_private_mean()))


     print("These are the student who passed the course")
     print("Normal: " + str(rep.calc_students_passed(50)))
     print("Epsilon 0.4: " + str(pr_1.calc_private_students_passed(50)))
     print("Epsilon 0.7: " + str(pr_2.calc_private_students_passed(50)))

     print("These are the student who failed the course")
     print("Normal: " + str(rep.calc_students_failed(50)))
     print("Epsilon 0.4: " + str(pr_1.calc_private_students_failed(50)))
     print("Epsilon 0.7: " + str(pr_2.calc_private_students_failed(50)))




     # Data for x-axis (assuming each distribution has the same number of elements)
     x = range(len(list_normal))

     #     Plotting the bar chart
     plt.figure(figsize=(8, 6))

     plt.bar(x, list_normal, width=0.2, label='Original distribution', align='center')
     plt.bar([i + 0.2 for i in x], priv_list1, width=0.2, label='With Privacy Budget = 0.4', align='center')
     plt.bar([i + 0.4 for i in x], priv_list2, width=0.2, label='With Privacy Budget = 0.7', align='center')

     # Adding labels, title, and legend
     plt.xlabel('Bin grades')
     plt.ylabel('Count of Grades')
     plt.title("Original exam grade and and private distributions of 'Privacy Investments 101'")
     plt.xticks([i + 0.2 for i in x], ['<10', '<20', '<30', '<40', '<50', '<60', '<70', '<80', '<90', '<100'])  # Replace with your own labels
     plt.legend()

     plt.tight_layout()
     plt.show()



