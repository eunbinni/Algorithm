from collections import deque

graph = [
    [], # 0 비워둠
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

check = [False] * 9
def bfs(graph, start, ):
    q = deque([start])
    check[start] = True
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if check[i] == False:
                q.append(i)
                check[i] = True

bfs(graph, 1)