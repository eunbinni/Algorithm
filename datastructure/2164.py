from collections import deque

n = int(input())

lst = [i for i in range(1, n+1)]
lst = deque(lst)

while len(lst) > 1:
    p = lst.popleft()
    if len(lst) > 1:
        s = lst.popleft()
        lst.append(s)

print(lst.popleft())