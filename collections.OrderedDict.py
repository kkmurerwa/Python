from collections import OrderedDict

sold_items = OrderedDict()
number = int(input())

for i in range(number):
    text_input = input().split()
    price = text_input[-1]#Adds the last value to variable price
    label = ' '.join(text_input[:-1])#Joins remaining characters to form label
    if label in sold_items:
        sold_items[label] += int(price)
    else:
        sold_items[label] = int(price)
for i in sold_items:
    print(i, sold_items[i])
