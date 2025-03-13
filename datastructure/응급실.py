from collections import deque

n, m = map(int, input().split())
lst = list(map(int, input().split()))

queue = deque([(idx, value) for idx, value in enumerate(lst)])
# print(queue)
cnt = 0
answer = []
# 내 풀이
while queue:
    i, v = queue.popleft()
    flag = False
    for idx, value in queue:
        if v < value:
            queue.append((i, v))
            flag = True
            break
    if not flag:
        cnt += 1
    if i == m:
        answer.append(cnt)
print(answer[-1])

# 더 좋은 풀이
while queue:
    p = queue.popleft()
    if any(p[1] < x[1] for x in queue):
        queue.append(p)
    else:
        cnt += 1
        if p[0] == m:
            break
print(cnt)