import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # n = 4(세로) , m = 5(가로)

graph = [] # 이중리스트
for _ in range(n):
    graph.append(list(map(int, input().strip())))

def dfs(x, y):
    if 0 <= x < n and 0 <= y < m: # 범위 체크
        if graph[x][y] == 0: # 방문하지 않았다면
            graph[x][y] = 1 # 방문처리
            dfs(x-1, y) # 상
            dfs(x+1, y)# 하
            dfs(x, y-1)# 좌
            dfs(x, y+1)# 우
            return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)




