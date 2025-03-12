# 프로그래머스 가장 큰 수와 문제 다름

n,remove = map(int, input().split())
lst = list(map(int, str(n)))
result = 0
cnt = 0
stack = []
for x in lst:
    while stack and stack[-1] < x and cnt < remove:
        stack.pop()
        cnt += 1
    stack.append(x)
    # print(stack, cnt)

if cnt < remove:
    m = remove-cnt
    stack = stack[:-m]
for x in stack:
    print(x, end = '')
# 5276823 3