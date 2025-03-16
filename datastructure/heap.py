import heapq

# default: min heap
# heap = []
# while True:
#     n = int(input())
#     if n == 0:
#         print(heapq.heappop(heap))
#     elif n == -1:
#         break
#     else:
#         heapq.heappush(heap, n)
#         print(heap)

# max heap
heap = []
while True:
    n = int(input())
    if n == 0:
        minus, plus = heapq.heappop(heap)
        print(plus)
    elif n == -1:
        break
    else:
        heapq.heappush(heap, (-n, n))
        # print(heap)