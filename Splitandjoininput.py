def split_and_join(line):
    newline = line.split(" ")
    newline = "-".join(newline)
    return newline

line = input()
result = split_and_join(line)
print(result)