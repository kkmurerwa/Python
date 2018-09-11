#Numpy array manipulations
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.shape(a)#Shows number of rows and columns in the array
print (b)
print("")

a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)#Reshapes the array and outputs it in the prescribed style
print(b)

#print(b.itemsize()) #Should output the size of the array

#One can create an empty numpy array using numpy.empty

empty_array = np.empty([3, 2], dtype=float)
print(empty_array)

#one can also create a zeros array where all the default values are zeros

x = np.zeros((2,2), dtype=[('x', 'i4'), ('y', 'i4')])
print(x)
print()

#A similar thing can be done using a ones array

x = np.ones((2,2), dtype=[('x', 'i4'), ('y', 'i4')])
print(x)
print()
