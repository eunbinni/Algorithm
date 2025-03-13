from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])
cnt = 0
while len(queue) > 1:
    p = queue.popleft()
    cnt += 1
    if cnt == k:
        cnt = 0
    else:
        queue.append(p)
print(queue[0])
#
# # 더 좋은 풀이
# while queue:
#     for _ in range(k-1): # k = 3, 2번 빼고
#         p = queue.popleft()
#         queue.append(p)
#     queue.popleft()
#     if len(queue) == 1:
#         print(queue[0])
#         break
