#This code checks is an input is a regular expression or not. Input is in format below
#2
#.*\+
#.*+

import re

no_of_inputs = int(input())

for i in range(no_of_inputs):
    raw_string = input()
    try:
        re.compile(raw_string)
        print(True)
    except re.error:
        print(False)