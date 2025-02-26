import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)] # 0번쨰 비워두기
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
def bfs(start, visited):
    cnt = 0
    q = deque([start])
    # v = q.popleft() # 맨 앞의 원소 빼기
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]: # i = 2
            if not visited[i]:
                cnt += 1
                q.append(i) # 2
                visited[i] = True
    return cnt
print(bfs(1, visited))