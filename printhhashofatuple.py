n = int(input())
integer_tuple = tuple(map(int, input().split()))
hashtuple = hash(integer_tuple)
print(hashtuple)