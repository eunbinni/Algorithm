import sys

input = sys.stdin.readline

n = int(input().strip())

## 직접 빈 array 만들기
# a가 들어올 수 있는 값이 10000으로 한정되어 있기 때문에 빈 배열은 10001까지 만들면 됨
arr = [0] * 10001

for _ in range(n):
    a = int(input().strip())
    arr[a-1] = arr[a-1] + 1
    # a = 5, arr[5] = 1, arr = [0,0,0,0,1]
    # a = 2, arr[2] = 1, arr = [0,0,1,0,1]
    # a = 2, arr[2] = 2, arr = [0,0,2,0,1]
    # a = 3, arr[3] = 1, arr = [0,0,2,1,1]

# 값에 개수를 보관하고 인덱스를 출력
for i in range(n):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)