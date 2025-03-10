n = int(input())
A = list(map(int, input().split()))

dp = [0] * (n+1)
A.insert(0, 0) # 첫번째 인덱스
dp[1] = 1
answer = 0
for i in range(2, n+1):
    maxv = 0
    for j in range(i-1, 0, -1):
        if A[i] > A[j] and dp[j] > maxv: # 전에 있던 값들 중에서 최댓값 찾기
            maxv = dp[j]
    dp[i] = maxv + 1
    if dp[i] > maxv:
        answer = dp[i]
print(answer)

"""
dp = [1] * (n+1)
for i in range(1, len(A)):
    for j in range(i):
        if A[i] > A[j]: # 새로 올 값이 크다면
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))

"""