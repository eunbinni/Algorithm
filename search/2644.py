"""
dfs
"""
import sys

input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
result = []
def dfs(v, num, visited):
    visited[v] = True
    num += 1
    if v == y:
        result.append(num)
    for i in graph[v]:
        if not visited[i]:
            dfs(i, num, visited)

dfs(x, 0, visited)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)

