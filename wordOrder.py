from collections import OrderedDict

word_items = OrderedDict()
number = int(input())

for i in range(number):
    word = input()
    if word in word_items:
        word_items[word] += 1
    else:
        word_items[word] = 1
print(len(word_items))
for i in word_items:
    print(word_items[i],end=' ')
