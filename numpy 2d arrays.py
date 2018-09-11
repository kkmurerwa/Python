import numpy as np

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d.shape)#Outputs the number of rows and columns in an array
print(np_2d[0])#Outputs first row
print(np_2d[0, 1])#Outputs second item in first row
print(np_2d[:, 1:3])#Outputs second and third items in each row. This is called subsetting