n, m = map(int, input().split())

path = []
def dfs(level):
    if level == m:
        print(' '.join(map(str, path)))
        return
    for i in range(1, n+1):
        path.append(i)
        dfs(level + 1)
        path.pop()

dfs(0)