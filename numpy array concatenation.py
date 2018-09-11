import numpy as np
#This code concatenates inputed dimensions of the form
#4 3 2
#1 2
#1 2
#1 2
#1 2
#3 4
#3 4
#3 4
N, M, P = map(int, input().split())
list_one = []
list_two = []
for i in range(N):
    list_one.append(list(map(int, input().split())))
for i in range(M):
    list_two.append(list(map(int, input().split())))

numpy_final_list_one = np.array(list_one).reshape(N, P)
numpy_final_list_two = np.array(list_two).reshape(M, P)
concat_list = np.concatenate((numpy_final_list_one, numpy_final_list_two))
print(concat_list)