n = int(input())

dp = [-1] * 100000
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    # print('i:', i, dp[i])
print(dp[n])

# recursion
def fib(n):
    if dp[n]>0:
        return dp[n] # 값 있으면 바로 리턴, 가지 뻗지 말고
    if n<2:
        return n
    dp[n] = fib(n-1) + fib(n-2)
    return dp[n]
print(fib(n))