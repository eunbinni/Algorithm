import sys
input = sys.stdin.readline
n, m = map(int, input().split())

poket = {}
poket2 = {}
for i in range(1, n+1):
    p = input().strip()
    poket[p] = i
    poket2[i] = p

for _ in range(m):
    x = input().strip()
    if x.isdigit():
        print(poket2[int(x)])
    else:
        print(poket[x])

"""
아니 이렇게 쉬운 문제에서 dict value값 찾으려고 for문을 쓰다니?
dict 두개 만들면 되잖아!!!!!!!!! 해시테이블 O(n) 쓰는 의미가없잖아~
"""