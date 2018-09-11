from collections import Counter
#Imports counter function from collections

shoes = int(input())
shoe_sizes = input().split()
shoe_count = Counter(shoe_sizes)
cust = int(input())
sales = 0
for i in range (0,cust):
    index, cash = input().split()
    cash = int(cash)
    if index in shoe_sizes:
        if (shoe_count[index]>0):
            shoe_count[index] -= 1
            sales += cash

print(sales)


