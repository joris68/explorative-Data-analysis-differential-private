import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n_bins = 10
x = np.random.randn(1000, 3)
print(x)

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = [100, 200, 300, 400, 500]

# Combine the three lists element-wise using zip
combined_lists = [list(item) for item in zip(list1, list2, list3)]
print(combined_lists)

