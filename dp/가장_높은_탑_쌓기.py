n = int(input())
dp= [0] * n
bricks = []
for _ in range(n):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c))

bricks.sort(reverse = True)
bricks.append((0, 0, 0))
# print(bricks)
# print(bricks[0][1])
dp[0] = bricks[0][1]
for i in range(n):
    maxv = 0
    for j in range(i-1, -1, -1): # 인덱스 -1까지 주의하기, 0번째 idx까지 확인해야함
        if bricks[i][2] < bricks[j][2]:
            maxv = max(maxv, dp[j])
    dp[i] = maxv + bricks[i][1]
print(dp)
print(max(dp))
"""
정렬 내림차순이니까 (0, 0, 0)이 맨 뒤로 가서
어차피 0번째 index까지 확인해야하는것은 동일함
"""

