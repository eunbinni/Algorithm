from collections import deque
n = 7
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result = 0
def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        print(y, x)
        if y == n - 1 and x == n - 1:
            return graph[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<=n-1 and 0<=nx<=n-1 and graph[ny][nx]==0:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    graph[ny][nx] = graph[y][x] + 1
                    print(graph[ny][nx])
    return -1
print(bfs(0, 0))

"""
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0
"""