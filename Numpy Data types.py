#Numpy Data types
import numpy as np
string_num = "548946161145"

print(np.int64(string_num)**np.int64(string_num))#This is a string of 64bytes
print(np.bool_(int(string_num) > 150))#This is a numpy boolean

#dtype is used to convert data into any type eg.
dt = np.dtype([('age', np.int8)])#creates a custom data type or struct. Below is a simple struct
a = np.array([(10), (20), (30)], dtype=dt)
print (a['age'])

#dtype as a multiple information struct
student=np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
#In the struct above, S20 is a string of 20 items, i1 is an integer of one digit and f4 is a float of 4 digits
b = np.array([('kenneth', 5, 10.20), ('joseph', 4, 14.01)], dtype = student)
print(b['name'])
#Other data types that can be used in the student struct are "b = boolean, i = integer
#u = unsigned integer, f = floating, c = complex floating, m = timedelta, M =  datetime,
#O = python objects, S, a = string, U = unicode, V = raw data