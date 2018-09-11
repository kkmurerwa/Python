def solve(name):
    newname = name.split(' ')
    templist = []
    finalname = ""
    print(newname)
    for i in newname:
        #This method converts the first letter to caps
        if (i.isalnum()):
            temp = list(i)
            temp[0] = temp[0].upper()
            newstring = ''.join(temp)
            templist.append(newstring)
        else:
            templist.append('')
    for i in range(0,(len(templist))):
        finalname += templist[i]
        if (i < (len(templist)-1)):
            finalname += " "
    return finalname

s = input()
print(solve(s))