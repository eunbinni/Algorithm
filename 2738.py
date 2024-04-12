n, m = map(int, input().split())
# n : 행
# m : 열

A = []
B = []

for _ in range(n):
    data = list(map(int, input().split()))
    A.append(data)

for _ in range(n):
    data = list(map(int, input().split()))
    B.append(data)

for i in range(n):
    row = [] # list 활용하여 row 값 담아두기
    for j in range(m):
        row.append(A[i][j] + B[i][j]) # [1,2,3]
    print(' '.join(map(str, row))) # ['1', '2', '3']을 join