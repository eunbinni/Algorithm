"""
1. 아이디어
- 2중 for문 -> graph가 1이고 방문하지 않았을 때만 저장
- BFS 돌면서 그림의 개수 +1, 그림의 넓이 계산

2. 시간복잡도
- O(V+E)
- V : m * n
- E : V * 4 (하나의 Vertex 당 4개의 edge 연결이라고 가정)
- O(V+E) = V + E = V + 4V = 5V = 5mn = 5 * 500 * 500 =
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)

"""
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# print(graph)
chk = [[False] * m for _ in range(n)]
queue = []

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x):
    rs = 1 # 그림의 넓이
    q = deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft() # 원소 뽑기
        for k in range(4): # 네방향
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m: # 사이즈를 넘어가지 않는 경우
                if graph[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs

cnt = 0 # 그림 개수
maxv = 0 # 그림 넓이, 한칸씩 옮길때마다 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            cnt += 1
            # BFS 결과 최댓값 크기 갱신
            maxv = max(maxv, bfs(i,j))
print(cnt)
print(maxv)


