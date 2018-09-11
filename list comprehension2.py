import re

text = "inspam"
pattern = r"pam"

#RegEx search returns an object that can further be manipulated
match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())#Returns the pattern being searched for
    print(match.start())#Returns the start value of the matching substring
    print(match.end())#Returns the end value of the matching substring
    print(match.span())#Returns the indices of the matching substring

if re.search(pattern, text):#re.search returns True if the pattern matches any character in the string
    print(True)
else:
    print(False)

if re.findall(pattern, text):#re.findall returns a set of all the string slices in the string that match the pattern
    print(True)
    print(re.findall(pattern, text))
else:
    print(False)

#This replaces all occurences of "David" with Amy
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)