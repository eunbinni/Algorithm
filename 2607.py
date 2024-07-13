"""
len(compare) <= 1 조건을 생각 못함
["D", "O", "O"] 같은 예시가 해당
"""

import sys
input = sys.stdin.readline

n = int(input().strip())

first_word = list(input().strip()) # 기준 단어

final = 0
for _ in range(n-1):
    compare = first_word[:] # 첫번째 단어 복사
    word = list(input().strip()) # 단어 하나씩 바로 입력 받으면서 확인
    cnt = 0
    for string in word: # 두번째 단어부터 하나씩 확인
        if string in compare: # 첫번째 string list 안에 있다면
            compare.remove(string)
        else:
            cnt += 1
    if cnt <= 1 and len(compare) <= 1:
        final += 1
print(final)