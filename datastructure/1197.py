import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
# create adj list
for _ in range(v+1):
    a, b, c = map(int, input().split())
    graph[a].append([c, b]) # (edge, vertex)
    graph[b].append([c, a])

heap = [[0,1]]
result = 0
while heap:
    w, each_node = heapq.heappop(heap)
    if not visited[each_node]:
        visited[each_node] = True
        result += w
        for next_edge in graph[each_node]: # 노드에 붙은 간선 확인
            if not visited[next_edge[1]]:
                heapq.heappush(heap, next_edge)
print(result)
