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

# print(graph)

from collections import deque
visited = [False] * (n+1)
queue = deque()
parent = [0] * (n+1)
def bfs(v):
    queue.append(v)
    visited[v] = True
    while queue:
        p = queue.popleft()
        for x in graph[p]:
            if not visited[x]:
                visited[x] = True
                # print(x)
                parent[x] = p
                queue.append(x)
bfs(1)
for x in parent[2:]:
    print(x)