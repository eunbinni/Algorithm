n = int(input())

max_num, min_num = float('-inf'), float('inf')
# prev_max_num, prev_min_num = float('-inf'), float('inf')
graph = []
for j in range(n):
    tmp = list(map(int, input().split()))
    for i in range(n):
        if tmp[i] < min_num:
            min_num = tmp[i]
            start_x = i # 조심
            start_y = j
        if tmp[i] > max_num:
            max_num = tmp[i]
            end_x = i
            end_y = j
    graph.append(tmp)

visited = [[False] * n for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0

def dfs(y, x):
    global cnt

    if y == end_y and x == end_x:
        cnt += 1
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<=n-1 and 0<=nx<=n-1 and not visited[ny][nx]:
            if graph[y][x] < graph[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx)
                visited[ny][nx] = False # 백트래킹

dfs(start_y, start_x)
print(cnt)
"""
5
2 23 92 78 93
59 50 48 90 80
30 53 70 75 96
94 91 82 89 93
97 98 95 96 100
"""