"""
최단경로 보장하는 bfs 사용
"""
from collections import deque

def solution(maps):
    m = len(maps)
    n = len(maps[0])
    visited = [[False] * n for _ in range(m)]
    dy = [-1, 0, 1, 0]  # 상우하좌
    dx = [0, 1, 0, -1]

    def bfs(y, x):
        cnt = 1
        queue = deque([(y, x)])
        visited[y][x] = True
        while queue:
            print(queue)
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < m and 0 <= nx < n and maps[ny][nx] == 1 and not visited[ny][nx]:
                    print(ny, nx)
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1
        return maps[m - 1][n - 1]

    if bfs(0, 0) == 1:
        return -1
    else:
        return maps[m - 1][n - 1]

# 두번째 풀이
from collections import deque

# 최단경로 bfs, 칸 수를 세는 부분 중요
# n: 가로, m: 세로

def solution(maps):
    answer = 0
    n = len(maps[0])
    m = len(maps)
    graph = [[] for _ in range(m + 1)]
    visited = [False] * (m + 1)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]  # 시계방향, 상, 우, 하, 좌

    def bfs(y, x):
        queue = deque()
        queue.append([y, x])

        while queue:
            y, x = queue.popleft()
            # print(y, x)
            if y == m - 1 and x == n - 1:
                return maps[y][x]

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < m and 0 <= nx < n and maps[ny][nx] == 1:  # 이동 가능
                    maps[ny][nx] = maps[y][x] + 1
                    print(ny, nx, maps[ny][nx])
                    queue.append([ny, nx])

        if y != m - 1 or x != n - 1:
            return -1

    answer = bfs(0, 0)

    return answer