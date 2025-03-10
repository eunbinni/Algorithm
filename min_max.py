import sys
# 최솟값
lst = [1,5,3,6,67,1,542,61,23]
min_num = sys.maxsize
# min_num = float('inf')
for x in lst:
    if x < min_num:
        min_num = x
print(min_num)

# 최댓값 '-inf' 해야 음수도 찾을 수 있음
max_num = float('-inf')
for x in lst:
    if x > max_num:
        max_num = x
print(max_num)
"""
리스트에서 최댓값, 최솟값 찾는 상황에서는
max(), min()이 더 좋음
"""