import bisect
n, m = map(int, input().split())

lst = [input() for _ in range(n)]
lst2 = [input() for _ in range(m)]

lst.sort()
def binary_search(target):
    start = 0
    end = len(lst) - 1 # 인덱스라서 -1 주의해야함
    while start <= end:
        mid = (start + end) // 2
        if lst[mid].startswith(target):
            return True
        elif lst[mid] < target:
            start = mid+1
        else:
            end = mid - 1
    return

cnt = 0
for x in lst2:
    if binary_search(x):
        cnt += 1
print(cnt)


# python bisect 활용
"""
cnt = 0
for x in lst2:
    idx = bisect.bisect_left(lst, x) # lst에서 x를 찾아서 idx로 반환
    if idx < n and lst[idx].startswith(x):
        cnt += 1
print(cnt)

"""



"""
시간초과코드

cnt = 0
for y in lst2:
    for x in lst:
        n = len(y)
        if y == x[:n]:
            cnt += 1
            break
print(cnt)

"""