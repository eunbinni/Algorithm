import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
m = int(input())
lst2 = list(map(int, input().split()))
def search(start, end, target):
    mid = (start + end) // 2
    if start == end:
        if lst[start] == target:
            print("1")
        else:
            print("0")
        return
    if lst[mid] < target:
        search(mid+1, end, target)
    else:
        search(start, mid, target)

for x in lst2:
    search(0, n-1, x)

"""
def binarySearch(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2 # 몫
    if target == array[mid]:
        return 1
    elif target > array[mid]:
        return binarySearch(array, target, mid+1, end)
    else:
        return binarySearch(array, target, start, mid-1)

for i in M:
    print(binarySearch(A, i, 0, len(A)-1))

"""