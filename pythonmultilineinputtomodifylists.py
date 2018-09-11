N = int(input())
arraylist = []
for i in range(N):
    command, *line = input().split()
    arraydoer = list(map(int,line))
    if (command=="insert"):
        arraylist.insert(arraydoer[0],arraydoer[1])
    elif (command=="remove"):
        arraylist.remove(arraydoer[0])
    elif (command=="append"):
        arraylist.append(arraydoer[0])
    elif (command=="sort"):
        arraylist = sorted(arraylist)
    elif (command=="print"):
        print(arraylist)
    elif (command=="pop"):
        arraylist.pop(-1)
    elif (command=="reverse"):
        arraylist.reverse()