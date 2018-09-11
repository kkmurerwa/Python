from itertools import permutations

inputted, times = input().split()#Split the input
times = int(times)#Turn the times input to int for use by the permutation function
input_list = sorted(list(inputted))#Turns the input to list and sorts it in alphabetical order
output_list = list(permutations(input_list, times))#Finds permutations and stores them as list
for i in output_list:#Outputs the permutations line by line
    i = list(i)
    output_list2 = (''.join(i)).upper()
    print(output_list2)


