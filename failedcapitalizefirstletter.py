def solve(name):
    newname = name.split()
    templist = []
    finalname = ""
    for i in newname:
        temp = list(i)
        temp[0] = temp[0].upper()
        newstring = ''.join(temp)
        templist.append(newstring)
    for i in range(0,(len(templist))):
        finalname += templist[i]
        if (i < (len(templist)-1)):
            finalname += " "
    return finalname

s = input()
print(solve(s))