"""
최소비용 구하기 : 전형적인 다익스트라 알고리즘
"""
import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
heap = []
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

start, end = map(int, input().split())
dist = [float('inf')] * (n+1)

heapq.heappush(heap, (0, start))
dist[start] = 0
while heap:
    w, v = heapq.heappop(heap)
    if dist[v] != w: # w는 이전에 힙에 저장해뒀던 최단거리니까 갱신할 필요 없어서 continue
        continue
    for nw, nv in graph[v]:
        if dist[nv] > dist[v] + nw:
            dist[nv] = dist[v] + nw
            heapq.heappush(heap, (dist[nv], nv))
# print(dist)
print(dist[end])