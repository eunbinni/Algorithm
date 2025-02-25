from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    queue = deque([])
    for idx, value in enumerate(lst):
        queue.append((idx, value))

    cnt = 0
    while queue:
        p = queue.popleft()
        higher_priority_exists = False
        # if any(p[1] < q[1] for q in queue): # 뒤에 더 높은 순위가 있다면 다시 넣음, 카운트 증가시키지 않음
        for q in queue:
            if p[1] < q[1]:
                queue.append(p)
                higher_priority_exists = True
                break
        if not higher_priority_exists: # p가 제일 높은 순서일 때
            cnt += 1
            if p[0] == m:
                break
    print(cnt)
