import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
maxv = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [[False] * m for _ in range(n)]

def bfs(y, x):
    size = 1
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=ny<n and 0<=nx<m: # from 0 to n-1
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    size += 1
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return size

for j in range(n): # y
    for i in range(m): # x
        if graph[j][i] == 1 and not visited[j][i]:
            cnt += 1
            maxv = max(maxv, bfs(j, i))
print(cnt)
print(maxv)