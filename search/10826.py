import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split())) # 가지고 있는 카드 리스트
m = int(input())
arr2 = list(map(int, input().split())) # 비교해야 할 카드 리스트

arr.sort()

dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
arr = list(dic.keys())

def binary_search(arr, start, end, target):
    start = 0
    end = len(arr)-1
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return

for i in arr2:
    if binary_search(arr, 0, n, i):
        print(dic[i], end = ' ')
    else:
        cnt = 0
        print(cnt, end = ' ')