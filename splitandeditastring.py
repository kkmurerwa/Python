def mutate_string(string, position, character):
    listedstring = list(string)
    listedstring[position] = character
    newstring = ''.join(listedstring)
    return newstring

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)