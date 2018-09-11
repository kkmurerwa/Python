from operator import itemgetter#Imports itemgetter class ordering nested lists

def Remove(duplicate):
    ''' This method removes duplicates from any fed argument'''
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

students = []
scores = []
for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])#Adds names of students to the student list
        scores.append(score)#Adds scores to score list for easier manipulation

nodups = list(Remove(scores))#Removes duplicate scores to maintain a clear order
nodups.sort()
runnerup = nodups[1]#Finds second-lowest grade
alphabeticalnames = []
for i in students:
    if ((i[1])==runnerup):
        alphabeticalnames.append(i[0])#Adds names of people with second-lowest grade to list

alphabeticalnames.sort()#Sorts names of people with second-lowest grade alphabetically
for i in alphabeticalnames:
    print(i)

