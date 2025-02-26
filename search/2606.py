import sys
from collections import deque

input = sys.stdin.readline

m = int(input()) # 컴퓨터 수(노드 수)
n = int(input()) # 네트워크 수

visited = [False] * (m+1) # 노드 개수 +1

graph = [[] for _ in range(m+1)] # 이차원 빈 배열

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 연결 리스트
# print(graph)
def bfs(start):
    cnt = 0
    q = deque([start])
    visited[start] = True ### 처음 노드 방문 처리 중요
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                cnt += 1
                visited[i] = True
    return cnt

print(bfs(1))

