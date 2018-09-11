import numpy as np
import scipy
import matplotlib
height = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height = np.array(height)#Converts the list to a numpy array
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_weight = np.array(weight)
bmi = np_weight / np_height **2#numpy arrays can be multiplied against each other unlike lists
print(bmi)

#Numpy libraries, unlike python lists, when added, output the sum of items in the same
#index while python lists are concatenated

python_list = [1, 5, 6, 8]
print(python_list+python_list)
numpy_array = np.array(python_list)
print(list(numpy_array+numpy_array))

#Numpy can also be used to analyze data and return boolean values for each item in the numpy array

numpy_weight = np.array(weight)
values = list(numpy_weight>63.0)
print(values)