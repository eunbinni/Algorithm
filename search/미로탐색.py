
n = 7
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0
visited[0][0] = True
def dfs(y, x):
    global cnt
    if y == n-1 and x == n-1:
        cnt += 1 # 도착점에 와서 cnt +=1 하고, 백트래킹
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<n and 0<=nx<n and graph[ny][nx] == 0:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                print(ny, nx)
                dfs(ny, nx)
                visited[ny][nx] = False ##### 중요

dfs(0, 0)
print(cnt)

"""
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0
"""