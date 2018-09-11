import numpy as np

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d.dtype)#Returns the type of data in the array

print(np.round(np_2d[0, 3], 1))#This rounds the number to the specified number of decimals

#numpy supports numerous types of number. These are specified using the dtype parameter of array

array_complex = np.array([1.+3.j, 2. + 8.j, 3. - 2.j], dtype=complex)
#The numbers above have to be written in the shown form to be deduced as complex

print(array_complex)