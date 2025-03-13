n = int(input())

word = {}
# hash 사용
for i in range(n):
    x = input()
    word[x] = 1

for i in range(n-1):
    x = input()
    word[x] = 0

for value, cnt in word.items():
    if cnt == 1:
        print(value)