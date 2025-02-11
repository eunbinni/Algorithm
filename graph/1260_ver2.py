from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

visited = [False] * (n+1) # 1d list

def dfs(visited, graph, v):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(visited, graph, i)

dfs(visited, graph, v)
print()
def bfs(visited, graph, v):
    queue = deque([v])
    visited[v] = True
    while queue:
        a = queue.popleft()
        print(a, end = ' ')
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False] * (n+1) # 1d list
bfs(visited, graph, v)