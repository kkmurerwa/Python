from itertools import combinations

string, iterations = input().split()
iterations = int(iterations)
string_list = list(string.upper())


string_list.sort()
for i in range (1,iterations+1):
    for item in combinations(string_list, i):
        print(''.join(item))