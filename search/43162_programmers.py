# 프로그래머스 네트워크 https://school.programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    # from adj matrix to adj list
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i + 1].append(j + 1)

    def dfs(v):
        visited[v] = True
        for x in graph[v]:
            if not visited[x]:
                dfs(x)

    def bfs(v):
        visited[v] = True
        queue = deque([v])
        while queue:
            p = queue.popleft()
            for i in graph[p]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    for i in range(1, n + 1):
        if not visited[i]:
            print(i)
            # dfs(i)
            bfs(i)
            answer += 1

    return answer