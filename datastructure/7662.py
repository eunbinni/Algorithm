import heapq
import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    entry = defaultdict(int)

    for _ in range(k):
        command, num = input().split()
        num = int(num)
        if command == "I": # heap push
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
            entry[num] += 1
        elif command == "D":
            if num == -1: # 최솟값
                while min_heap and entry[min_heap[0]] == 0: # 이미 삭제된 원소 삭제하는 과정
                    heapq.heappop(min_heap)
                if min_heap:
                    a = heapq.heappop(min_heap)
                    entry[a] -= 1
            else: # 최댓값 제거
                while max_heap and entry[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    b = -heapq.heappop(max_heap)
                    entry[b] -= 1
    # 최종 제거를 위해
    while max_heap and entry[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and entry[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")

"""
elif x == "D 1":
    max_heap = [-x for x in heap[:]] # 시간복잡도 초과
    heapq.heapify(max_heap)
    heap.remove((-heapq.heappop(max_heap)))

- 위 코드가 프로그래머스에서는 효율성 통과를 하지만 백준 7662에서는 시초가 난다.
"""