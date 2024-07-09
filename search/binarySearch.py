import sys

input = sys.stdin.readline
n, target = map(int, input().split()) # n : 전체 원소 개수, target : 목표
array = list(map(int, input().split()))

def binarySearch(array, target, start, end):
    if start > end: # 시작인덱스 > 끝인덱스
        return None
    mid = (start + end) // 2  # 몫
    if target == array[mid]:
        return mid+1 # 0부터 인덱스 계산 시 mid, # 1부터 인덱스 계산 시 mid+1
    elif target < array[mid]:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)

print(binarySearch(array, target, 0, n-1))
