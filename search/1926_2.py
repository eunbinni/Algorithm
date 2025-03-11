import sys
input = sys.stdin.readline

# n: 세로, m: 가로 주의!!!!!!!
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)
visited = [[False] * m for _ in range(n)]
# print(visited)

dy = [-1, 0, 1, 0] # 상우하좌
dx = [0, 1, 0, -1]

# def dfs(y, x):
#     global size
#     # if y < 0 or y >= n or x < 0 or x>=m:
#     #     return
#     size += 1
#     visited[y][x] = True
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0<=ny<n and 0<=nx<m: # 이거 위치 빠지면 안됨, [ny][nx] index error 발생
#             if not visited[ny][nx] and graph[ny][nx] == 1:
#                 dfs(ny, nx)

def dfs_2(y, x):
    global size
    if y<0 or y>=n or x<0 or x>=m: # 종료 조건을 여기에 명시하면 됨
        return
    if visited[y][x] or graph[y][x]==0:
        return
    size += 1
    visited[y][x] = True
    dfs_2(y-1, x)
    dfs_2(y, x+1)
    dfs_2(y+1, x)
    dfs_2(y, x-1)

cnt = 0
max_size = 0
for j in range(n): # y 먼저 돌기
    for i in range(m):
        if not visited[j][i] and graph[j][i] == 1:
            size = 0 # dfs 새로 호출될때마다 갱신해야함
            # dfs(j, i)
            dfs_2(j, i)
            cnt += 1 # 그림의 개수
            max_size = max(size, max_size)

print(cnt)
print(max_size)


