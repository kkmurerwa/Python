from statistics import mean

n = int(input())
student_marks = {}
for _ in range(n):
    '''This loop splits the input to index and items. Index is name'''
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
scoreslist = student_marks[query_name]
print(format(mean(scoreslist),'.2f'))#Finds mean with the inbuilt function and rounds it off to 2dp