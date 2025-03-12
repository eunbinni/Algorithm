n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
start = 1 # 최소거리는 1이지
end = lst[-1]-lst[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    prev = lst[0]
    cnt = 1 # 첫번째 말 배치해야돼서 1로 설정
    for x in lst[1:]:
        if x-prev >= mid:
            cnt += 1
            prev = x
    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)


"""
for x in lst:
    path = abs(prev - x)
    if path > mid:
        cnt += 1
        prev = x
"""