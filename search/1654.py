
K, N = map(int, input().split())

lst = [int(input()) for _ in range(K)]

start = 0
end = max(lst)
cnt = 0
mid = 0
result = 0
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    if mid == 0:
        break
    for x in lst:
        cnt = (x // mid) + cnt
    if cnt >= N:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)