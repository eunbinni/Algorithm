from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in lst:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
cnt = 0
def bfs(v, graph, visited):
    global cnt
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                # print(queue)
                visited[i] = True

for i in range(1, n+1):
    if not visited[i]:
        bfs(i, graph, visited)
        cnt += 1
print(cnt)