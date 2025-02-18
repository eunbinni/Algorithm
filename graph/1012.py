import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input().rstrip())
# print(graph)
#
# def dfs(x, y):
#     if x < 0 or x >=m or y < 0 or y>=n:
#         return False
#     if graph[y][x] == 1: # 노드 아직 방문하지 않음
#         graph[y][x] = 0 # 방문 처리
#         dfs(x, y-1) # 상
#         dfs(x, y+1) # 하
#         dfs(x-1, y) # 좌
#         dfs(x+1, y) # 우
#         return True

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)
                return True

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().rstrip().split()) # m : 가로, n: 세로
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().rstrip().split())
        graph[j][i] = 1
        for i in range(n):
            for j in range(m):
                if dfs(j, i):
                    cnt += 1
    print(cnt)

