import sys
input = sys.stdin.readline

n = int(input())
A = [0, 1, 2] # 초기

for i in range(3, n+1):
    A.append((A[i-1] + A[i-2])%10007)

print(A[n])
