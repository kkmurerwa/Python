import numpy

def arrays(arr):
    python_list = list(map(float, arr))
    numpy_list = numpy.array(python_list)
    return numpy.array(sorted(numpy_list, key=abs, reverse=True), float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)