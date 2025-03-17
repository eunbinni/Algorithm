m, n = map(int, input().split())
lst = []
for _ in range(m):
    a, b = map(int, input().split())
    lst.append((a, b))

result = float('-inf')
print(lst)
def dfs(line, time, score):
    global result
    if time > n: # 제한시간 초과한 경우
        return
    if line == m:
        result = max(result, score)
        return
    dfs(line+1, time + lst[line][1], score + lst[line][0])
    dfs(line + 1, time, score)
dfs(0, 0, 0)
print(result)
"""
5 20
10 5
25 12
15 8
6 3
7 4
"""