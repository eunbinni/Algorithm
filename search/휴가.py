n = int(input())
time = []
price = []
for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    price.append(b)
result = 0
time.insert(0, 0)
price.insert(0, 0) # 인덱스 1부터 시작

def dfs(line, p):
    global result

    if line == n+1:
        result = max(p, result)

    if line+time[line] <= n+1:
        dfs(line+time[line], p+price[line]) # 상담 다 끝나고 그 금액을 받는다
    dfs(line+1, p) # 이건 선택 안하는거니까 1씩 증가시켜야함

dfs(1,0)
print(result)
"""
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
"""