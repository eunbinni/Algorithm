from collections import deque

n = int(input())

lst = [input().split() for _ in range(n)]
queue = deque([])
for x in lst:
    if x[0] == "push":
        queue.append(x[1])
    elif x[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    elif x[0] == "size":
        print(len(queue))
    elif x[0] == "empty":
        if not queue:
            print("1")
        else:
            print("0")
    elif x[0] == "front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif x[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print("-1")


