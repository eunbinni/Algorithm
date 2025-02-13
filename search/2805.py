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
        total = []
        for i in arr:
            if i > mid:
                total.append(i-mid)
            else:
                pass
        if sum(total) >= m:
            start = mid + 1
        else:
            end = mid - 1
        h.append(mid)
    return max(h)

print(binary_search(arr, 0, n, m))