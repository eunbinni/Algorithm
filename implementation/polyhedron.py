# 파이썬 알고리즘 문제풀이 입문
from collections import Counter
n, m = map(int, input().split())

# 1~n 1~m까지 나올 수 있음
lst = []
for i in range(1, n+1):
    for j in range(1, m+1):
        lst.append(i + j)

frequent = Counter(lst)

maxv = max(frequent.values())
for k, v in frequent.items():
    if v == maxv:
        print(k, end = ' ')