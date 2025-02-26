from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

def bfs(x, y):
    queue = deque([(x, y)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()

        if x == m-1 and y == n-1:
            return graph[y][x]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1: # can go
                    queue.append((nx, ny))
                    graph[ny][nx] = graph[y][x] +1

print(bfs(0, 0))

"""
안되는 코드
def bfs(x, y):
    cnt = 0
    queue = deque([(x, y, 1)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        if x == m-1 and y == n-1 : # end
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1: # can go
                    queue.append((nx, ny))
                    cnt += 1
                    graph[ny][nx] = 0
"""

"""
out of memory

def bfs(x, y):
    queue = deque([(x, y, 1)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y, cnt = queue.popleft()
        if x == m-1 and y == n-1 : # end
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1: # can go
                    queue.append((nx, ny, cnt+1))
                    graph[ny][nx] = 0

"""