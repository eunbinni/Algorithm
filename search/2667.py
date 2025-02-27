"""
아이디어:
- not visited & 1이면 size 증가

시간복잡도:
- O(V+E)
- Vertex: N * N
- Edge: 4V
- total: 5V = 5(25 * 25) = 3125
자료구조:
- 스택 or 재귀함수
- visited bool[][]
- graph int[][]
"""
import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
visited = [[False] * n for _ in range(n)]
graph = [list(map(int, input().strip())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global size
    # size += 1
    visited[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                size += 1
                dfs(ny, nx)
answer = []
for j in range(n):
    for i in range(n):
        if graph[j][i] == 1 and not visited[j][i]:
            size = 1
            dfs(j, i)
            cnt += 1
            answer.append(size)
print(cnt)
for x in sorted(answer):
    print(x)