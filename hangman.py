import random

file = open("sowpods.txt","r")
words_list = list(file.read().split())#Converts words in the sowpods to text by splitting accross whitespaces
random_number = random.choice(words_list)
random_number_list = list(random_number)
random_number_len = int((len(random_number_list)/3)*2)
gaps = []#Stores the indices for areas where the gaps will be
for i in range(0,random_number_len):
    temp = random.choice(range(len(random_number_list)))#Appends to list
    if temp in gaps:#This check prevents duplicate values in the Gaps list
        i -= 1
    else:
        gaps.append(temp)

random_number_list_copy = random_number_list
solutions_list = []
gaps.sort()

for i in gaps:
    solutions_list.append(random_number_list_copy[i])
    random_number_list_copy[i] = "__"

print(random_number_list_copy)
print(solutions_list)
print("")

for i in range(0,(len(gaps)+3)):
    guess = input("Enter a letter to guess\n").upper()
    if guess in solutions_list:
        print("You got that one right")
        #Enter some code here
        for position, item in enumerate(solutions_list):
            if item == guess:
                random_number_list_copy[gaps[position]] = guess

    else:
        print("Sorry. Wrong Guess")
        print(f"You have {(len(gaps)+3)-(1+i)} chances remaining")

    print(random_number_list_copy)
    if "__" not in random_number_list_copy:
        print("You win")
        break

file.close()