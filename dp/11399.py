N = int(input())

lst = list(map(int, input().split()))

lst.sort()
n = len(lst)
dp = [0] * n

dp[0] = lst[0]
for i in range(1, n):
    dp[i] = dp[i-1] + lst[i]

print(sum(dp))