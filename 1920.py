import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
A = sorted(A)
m = int(input())

M = list(map(int, input().split()))

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
