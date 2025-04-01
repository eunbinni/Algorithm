import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))

table = [0] * n
for i in range(n):
    table[i] = table[i-1] + lst[i]

for _ in range(m):
    a, b = map(int, input().split())

    if a-2 < 0:
        print(table[b - 1])
    else:
        print(table[b-1] - table[a-2])

"""
매번 케이스마다 누적합을 만드는건 안됨
한번만 만들어두고 재사용한다
"""