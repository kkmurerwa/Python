def swap_case(stringinput):
    liststring = list(stringinput)
    outputstring = ""
    for i in liststring:
        if (str.islower(i)):
            outputstring += i.upper()#Converts the lowercase characters into uppercase characters
        else:
            outputstring += i.lower()#Converts the uppercase characters into lowercase characters
    return outputstring
inps = input()
print(swap_case(inps))