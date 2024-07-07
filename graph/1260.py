import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split()) # 노드, 간선, 첫시작

graph = [[] for _ in range(n+1)] # 빈 이중 리스트, +1해주는거 잊지 말기

### 그래프 구성
for _ in range(m): # 노드의 수만큼이 아니라 간선의 수만큼 돌아야 하는 것
    a, b = map(int, input().split())  # 원소 두개씩 받기
    graph[a].append(b)
    graph[b].append(a)

### 방문여부 체크
visited = [False] * (n+1)
## 연결된 노드 정렬 (작은 번호부터 방문)
for node in graph:
    node.sort()

result = [] # 재귀함수라서 전역변수로 선언
def dfs(v):
    visited[v] = True
    result.append(str(v))
    for nextnode in graph[v]:
        if not visited[nextnode]:
            dfs(nextnode)
    return ' '.join(result)

print(dfs(v))

def bfs(start):
    result = []
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft() # v = 1
        result.append(str(v))
        for nextnode in graph[v]:
            if not visited[nextnode]:
                q.append(nextnode)
                visited[nextnode] = True
    return ' '.join(result)

visited = [False] * (n+1) # 방문 여부 초기화
print(bfs(v))