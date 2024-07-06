"""
1. 아이디어
- bfs
2. 시간복잡도
3. 자료구조
- 방문한 노드 찾는 bool[][]
- queue
- graph[][]
"""
import sys
from collections import deque

input = sys.stdin.readline

m = int(input())
# n = int(input())

# visited = [False] * m+1 # 노드들의 개수 +1

graph = [[] for _ in range(m+1)] # 이차원 배열

for i in range(m):
    a, b = map(int, input().split())
    print(graph[a] + [b])
    # print(graph[a])





