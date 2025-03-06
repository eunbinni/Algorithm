import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1) # 0 인덱스 안씀
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v]) # 가중치가 먼저와야 heap이 그걸 우선순위로 파악

dist[k] = 0 # 시작점 초기화
heap = [[0,k]] # 시작 heap

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew:
        continue # 거리 배열에 저장된 값이랑 내가 지금 뽑은 노드의 가중치 비교해서 다르면 안봐도됨
    for nw, nv in graph[ev]: # 현재 노드에서 연결된거 확인
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])