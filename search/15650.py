n, m = map(int, input().split())

lst = []
visited = [False] * (n+1)
sorted_set = set()
def backtracking():
    for i in range(1, n+1):
        if len(lst) == m:
            sorted_set.add(tuple(sorted(lst)))
            return
        if not visited[i]:
            lst.append(i)
            visited[i] = True
            backtracking()
            lst.pop()
            visited[i] = False

backtracking()
sorted_set = sorted(sorted_set)
for x in sorted_set:
    print(" ".join(map(str, x)))