import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())

graph = [[] for _ in range(n+1)]

for _  in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

visited = [False] * (n+1)
parent = [0] * (n+1)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            dfs(i)

dfs(1)
for x in parent[2:]:
    print(x)