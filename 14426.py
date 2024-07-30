import sys

input = sys.stdin.readline

n, m = map(int, input().split())

N = [input().strip() for _ in range(n)]

"""
1. N만큼 for문을 돌면서 M만큼 슬라이싱 하면서 접두사인지 아닌지 체크
2. 접두사 체크법 : for문으로 i를 하나씩 증가시키면서 확인
"""
result = 0
for i in range(m):
    first = input().strip()
    for string in N:
        if string[:len(first)] == first:
            result += 1
            break
print(result)