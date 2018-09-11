#This program encryts by adding a space at the second last letter of a string

#Test I have a story to tell to a lot of people
input_string_list = list(input("Enter your input to encrypt it\n").split())
final_list = []

for i in range(len(input_string_list)):
    temp_list = list(input_string_list[i])
    if i > 0:
        if (len(temp_list)>1):
            temp_list.insert(-1, " ")
        else:
            temp_list.insert(0," ")
    else:
        temp_list.append(" ")
    final_list.append(''.join(temp_list))

print(''.join(final_list))

file = open("encryptedtext.txt","w")
file.write(''.join(final_list))
file.close()
