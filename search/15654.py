n, m = map(int, input().split())

lst = list(map(int, input().split()))
path = []
lst.sort()
visited = [False] * n
def dfs():
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            path.append(lst[i])
            dfs()
            path.pop()
            visited[i] = False
dfs()