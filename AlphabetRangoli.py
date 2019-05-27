def printer(times):
    for j in range(0, times):
        print("-", end="")


def print_rangoli():
    iterationLimit = int(input())
    dictionaryString = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    dictionaryArray = dictionaryString.split()  #Convert string to array
    for j in range (iterationLimit-1, -1, -1):
        printer(j*2)
        print(dictionaryArray[iterationLimit-1], end="")
        for i in range (iterationLimit-2, j-1, -1):
            printer(1)
            print(dictionaryArray[i], end="")
        for k in range (j+1,iterationLimit):
            printer(1)
            print(dictionaryArray[k], end="")
        printer(j*2)
        print()
    for m in range (1,iterationLimit):
        printer(m*2)
        print(dictionaryArray[iterationLimit-1], end="")
        for i in range (iterationLimit-2, m-1, -1):
            printer(1)
            print(dictionaryArray[i], end="")
        for k in range (m+1,iterationLimit):
            printer(1)
            print(dictionaryArray[k], end="")
        printer(m*2)
        print()
print_rangoli()