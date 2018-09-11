s = input()

list_s = list(s)
alpha_num = False
alphabet = False
digit = False
lowercase = False
uppercase = False

for i in list_s:
    nimm = str(i)
    if (nimm.isalnum()):
        alpha_num = True
    if (nimm.isalpha()):
        alphabet = True
    if (nimm.isdigit()):
        digit = True
    if (nimm.islower()):
        lowercase =True
    if (nimm.isupper()):
        uppercase = True
print(alpha_num)
print(alphabet)
print(digit)
print(lowercase)
print(uppercase)

