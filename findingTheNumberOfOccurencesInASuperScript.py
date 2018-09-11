import re

string_input = input()
sub_string = input()
print(len(re.findall(f"(?={sub_string})",string_input)))