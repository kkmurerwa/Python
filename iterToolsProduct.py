from itertools import product

num1 = input().split()
first_list = list(map(int,num1))
num2 = input().split()
second_list = list(map(int,num2))
output = list(product(first_list,second_list))
for i in output:
    print(i, end=" ")