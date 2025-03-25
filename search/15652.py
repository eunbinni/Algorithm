n, m = map(int, input().split())
path = []

def dfs(level):
    if level == m:
        print(' '.join(map(str, path)))
        return

    for i in range(1, n+1):
        if not path or path[-1] <= i: # 마지막 값을 기준으로 i 보다 작아야 오름차순 수열이 됨
            path.append(i)
            dfs(level + 1)
            path.pop()
dfs(0)