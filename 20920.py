import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words_list = []
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words_list.append(word)

count = {}
# 딕셔너리로 개수 담기
for i in words_list:
    try:
        count[i] += 1
    except:
        count[i] = 1

def criteria(word):
    return (-count[word], -len(word), word)

for word in sorted(count, key = criteria):
    print(word)