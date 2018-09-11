#This decrypter works with the spaceEncrypter to convert back text to a readable format



file = open("encryptedtext.txt", "r")
input_string_list = list(file.read().split())
print(input_string_list)

final_list = []

for i in range(len(input_string_list)):
    temp_list = list(input_string_list[i])
    if i == 0:
        temp_list.append(" ")
    elif i > 1:
        if len(temp_list)>1:
            temp_list.insert(1," ")
        else:
            temp_list.append(" ")
    final_list.append(''.join(temp_list))

print(''.join(final_list))
file_another = open("decryptedtext.txt","w")
file_another.write(''.join(final_list))
file.close()