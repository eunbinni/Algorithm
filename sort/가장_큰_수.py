n = int(input())
market = list(map(int, input().split()))
market.sort()
m = int(input())
order = list(map(int, input().split()))

def binary_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target: # find
            return True
        elif arr[mid] > target: # 찾고자 하는 값이 중간값보다 앞에 있는 경우
            end = mid-1
        else:
            start = mid+1
    return False

for i in order:
    if binary_search(market, 0, len(market), i):
        print("yes")
    else:
        print("no")

"""
5
8 3 7 9 2
3
5 7 9
"""