n = int(input())
lst = list(map(int, input().split()))

dp = [0] * (n+1)
lst.insert(0, 0)
dp[1] = 1
for i in range(len(lst)):
    maxv = 0
    for j in range(i-1, 0, -1):
       if lst[i] > lst[j]:
           maxv = max(dp[j], maxv)
    dp[i] = maxv + 1 # dp[i] indentation 주의

print(max(dp))