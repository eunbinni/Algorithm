import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def binary_search(arr, start, end, target):
    start = 0
    end = max(arr)
    h = []
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            if i > mid:
                total = total + (i - mid) # 정수로 표현 가능
        if total >= m:
            start = mid + 1
            h.append(mid)
        else:
            end = mid - 1
    return max(h)

print(binary_search(arr, 0, n, m))