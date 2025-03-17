from collections import deque

s, e = map(int, input().split())
visited = [False] * (100000)
queue = deque()
queue.append((0, s))
cnt = 0
level = 0
while queue:
    level, cur = queue.popleft()
    lst = [-1, 1, 5]
    if cur == e:
        break
    for i in lst:
        next = cur + i
        if 0<=next<=e:
            if not visited[next]:
                visited[next] = True
                queue.append((level+1, next))

print(level)