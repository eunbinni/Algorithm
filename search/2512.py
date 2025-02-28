n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()
start = 0
end = max(arr)
total = 0
while start <= end:
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            total += i # 예산 더하기
        else:
            total += mid # 상한액 더하기
    if total < m:
        start = mid + 1
    else:
        end = mid - 1