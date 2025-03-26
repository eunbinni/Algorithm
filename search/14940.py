from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
lst = [[-1] * m for _ in range(n)]
# n: 세로, m: 가로
def bfs(y, x):
    queue = deque()
    queue.append([y, x])
    visited[y][x] = True
    lst[y][x] = 0
    while queue:
        y, x = queue.popleft()
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and graph[ny][nx] == 1:
                queue.append([ny, nx])
                visited[ny][nx] = True
                lst[ny][nx] = lst[y][x] + 1

for j in range(n):
    for i in range(m):
        if graph[j][i] == 2:
            bfs(j, i)

for j in range(n):
    for i in range(m):
        if graph[j][i] == 0:
            print(0, end = ' ')
        else:
            print(lst[j][i], end = ' ')
    print()