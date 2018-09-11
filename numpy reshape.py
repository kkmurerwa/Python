import numpy as np
#This code accepts nine input numbers and outputs it in a 3x3 array
raw_list = tuple(map(int, input().split()))
print(np.reshape(raw_list, (3, 3)))
