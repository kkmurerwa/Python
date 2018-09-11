import numpy as np

no_of_inputs, items_in_list = map(int, input().split())
arr1 = list(map(int, input().split()))
for i in range(no_of_inputs):
    arr_temp = list(map(int, input().split()))
    if i == 0:
        arr_sum = np.add(arr1, arr_temp)
        arr_sub = np.subtract(arr1, arr_temp)
        arr_mult = np.multiply(arr1, arr_temp)
        arr_div = np.floor_divide(arr1, arr_temp)#Does floor division
        arr_mod = np.mod(arr1, arr_temp)
        arr_pow = np.power(arr1, arr_temp)
    else:
        arr_sum += arr_temp
        arr_sub -= arr_temp
        arr_mult *= arr_temp
        arr_div //= arr_temp
        arr_mod %= arr_temp
        arr_pow **= arr_temp
print("[", end="")
print(arr_sum, end="")
print("]")
print("[", end="")
print(arr_sub, end="")
print("]")
print("[", end="")
print(arr_mult, end="")
print("]")
print("[", end="")
print(arr_div, end="")
print("]")
print("[", end="")
print(arr_mod, end="")
print("]")
print("[", end="")
print(arr_pow, end="")
print("]")