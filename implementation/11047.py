# greedy 인 이유
# Ai는 Ai - 1의 배수라는 조건으로 인해 항상 큰거부터 빼는것이 최적임

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst = sorted(lst, reverse = True)

cnt = 0
for x in lst:
    cnt = (k // x) + cnt
    k = k % x
print(cnt)

# cnt * x 할 필요없이 % 하면 되잖아..
"""
for x in lst:
    if x > k:
        pass
    else:
        cnt = k // x
        k = k - (cnt*x)
        answer += cnt
"""