# dp table
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(1, n): # 방향은 하나 뿐이라서 미리 설정
    dp[0][i] = dp[0][i-1] + arr[0][i]
    dp[i][0] = dp[i-1][0] + arr[i][0]
# print(dp)

for i in range(1, n):
    for j in range(1, n):
        minv = min(dp[i-1][j], dp[i][j-1])
        dp[i][j] = minv + arr[i][j]
print(dp[n-1][n-1])
#
# 3
# 3 3 5
# 2 3 4
# 6 5 2