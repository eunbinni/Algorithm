import sys
input = sys.stdin.readline

n = int(input())
lst = [tuple(map(int, input().strip().split())) for _ in range(n)]
lst = sorted(lst, key = lambda x:(x[1], x[0]))
cnt = 0
# x, y = lst[0]
y = 0
for a, b in lst:
    if y <= a:
        cnt += 1
        y = b
        # print(a, b)
print(cnt)

"""
lambda x:x[1]을 하면 나머지 같을땐 x[0]을 기준으로 정렬되는게 아닌가?
-> 아니고 x[1], x[0]을 해야됨, 아니면 원래 리스트 순서가 유지됨
"""