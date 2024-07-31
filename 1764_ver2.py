"""
다시 풀기 : 1회
intersection이 생각 안나서 & 로 품
&는 리스트 지원이 안되기 때문에 set로 감싸주는 것이 중요함
다른 방법 : intersection, 파이썬 내장 라이브러리
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listen = [input().strip() for _ in range(n)]
hear = [input().strip() for _ in range(m)]
listen = set(listen)
hear = set(hear)
intersection = listen & hear
# intersection = listen.intersection(hear)

print(len(intersection))
for name in sorted(intersection):
    print(name)