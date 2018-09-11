from collections import deque

N = int(input())
deque_list = deque()
for i in range(N):
    command, *line = input().split()
    arraydoer = list(map(int,line))
    if (command=="append"):
        deque_list.append(arraydoer[0])
    elif (command=="appendleft"):
        deque_list.appendleft(arraydoer[0])
    elif (command=="pop"):
        deque_list.pop()
    elif (command=="popleft"):
        deque_list.popleft()
    elif (command=="print"):
        print(deque_list)
for i in deque_list:
    print(i,end=' ')