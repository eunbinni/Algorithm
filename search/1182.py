n, s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
selected_count = 0
def dfs(level, total, selected_count):
    global cnt
    if level == n:
        if total == s and selected_count > 0:
            cnt += 1
        return

    dfs(level + 1, total + lst[level], selected_count+1)
    dfs(level + 1, total, selected_count) # 현재 원소 미포함

dfs(0, 0, 0)
print(cnt)
"""
total > s: return 안되는 이유
total이 5일때 이후에 음수 값이 나오면 음수를 더해서 s = 0으로 만들 수 있음
"""