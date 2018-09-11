import numpy as np
#This code accepts input of the array size and outputs the ones and zeros of the array of the given size
array_size = tuple(map(int, input().split()))

print(np.zeros(array_size, dtype=int))
print(np.ones(array_size, dtype=int))
