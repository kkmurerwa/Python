from collections import namedtuple
#Imports named tuple from collections

students = int(input())
tuple_indices = namedtuple('Label',input().split())
sum_of_all = 0

for i in range(students):
    in1, in2, in3, in4 = input().split()
    temp = tuple_indices(in1, in2, in3, in4)
    sum_of_all += int(temp.MARKS)

print(format((sum_of_all/students), ".2f"))
