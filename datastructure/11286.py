import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
"""
튜플로 넘겨줌, 앞에있는 원소를 기준으로 정렬되니까
"""
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))