# n = int(input())

n = 10
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dy = [0, 0, -1] # 우 좌 하
dx = [1, -1, 0]
start_x = 0
for i in range(n):
    if graph[9][i] == 2:
        start_x = i
        start_y = 9
def dfs(y, x):
    if y == 0:
        return x
    for i in range(3):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
            if graph[ny][nx] == 1:
                print(ny, nx)
                visited[ny][nx] = True
                result = dfs(ny, nx)
                if result is not None: ## 반환값 있어야함
                    return result
    return

visited[9][start_x] = True
print(dfs(9, start_x))

"""
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1
1 0 1 0 0 1 0 1 1 1
1 1 1 0 0 1 0 1 0 1
1 0 1 0 0 1 1 1 0 1
1 0 1 0 0 2 0 1 0 1
"""