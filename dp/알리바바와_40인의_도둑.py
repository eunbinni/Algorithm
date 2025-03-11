# dfs, top-down
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

dy = [1, 0]  # 하,우
dx = [0, 1]
def dfs(y, x):
    if y == n-1 and x == n-1:
        return graph[y][x]

    minv = float('inf')
    if dp[y][x] != -1: # memoization cut해야함!!! 중요
        return dp[y][x]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            minv = min(minv, dfs(ny, nx))

    dp[y][x] = minv + graph[y][x] # 값 더하기
    return dp[y][x]

print(dfs(0, 0))