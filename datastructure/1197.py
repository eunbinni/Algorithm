import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
result = 0
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

heap = [[0, 1]]
visited[0] = True
while heap:
    w, n = heapq.heappop(heap)
    if not visited[n]:
        visited[n] = True
        result += w
        for next_e in graph[n]:
            if not visited[next_e[1]]:
                heapq.heappush(heap, next_e)
print(result)