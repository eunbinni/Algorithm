n = int(input())

dp = [-1] * 100000
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    # print('i:', i, dp[i])
print(dp[n])
#
# # recursion
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(n))