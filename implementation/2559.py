import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

# 초기값 세팅
each = 0
for i in range(k):
    each += lst[i]
maxv = each

# 다음 인덱스 더해주고, 이전 인덱스 빼주기
for i in range(k, n):
    each += lst[i]
    each -= lst[i-k]
    maxv = max(each, maxv)
print(maxv)

# timeout code
"""
sum = 0
prev = 0  
for i in range(n):
    sum = 0
    for j in range(i, k+i):
        if k+i > len(lst):
            break
        sum = sum + lst[j]
    sum = max(prev, sum)
    prev = sum
print(sum)
"""

"""
sum_num, prev = 0, 0
for i in range(n):
    if i+k <= n:
        sum_num = sum(lst[i:i+k])
    sum_num = max(sum_num, prev)
    prev = sum_num
print(sum_num)
"""