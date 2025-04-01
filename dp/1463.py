n = int(input())

dp = [0] * (n+1)

"""
elif 쓰면 안됨 왜냐? 2와 3으로 모두 나눠떨어지는 경우 검사를 못함
"""
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i //3]+1)

print(dp[n])