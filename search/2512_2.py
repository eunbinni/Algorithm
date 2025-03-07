import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
lst = sorted(lst)
def binary_search(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for x in lst:
            if x < mid:
                total += x
            else:
                total += mid
        if total <= m:
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer

print(binary_search(0, max(lst)))

"""
money에 append 하는 과정 필요 없이
mid 값을 바로 return 해도 됨
이진탐색하면서 항상 최댓값을 보장하기 때문
"""
