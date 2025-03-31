t = int(input())
"""
재귀함수 호출해서 횟수를 계산하면 시간 초과
0, 1 등장 횟수만 계산하도록 dp table 만들기
"""

for _ in range(t):
    cnt_0, cnt_1 = 0, 0
    n = int(input())

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        dp_0 = [0] * (n + 1)
        dp_1 = [0] * (n + 1)
        dp_0[0] = 1
        dp_1[0] = 0
        dp_0[1] = 0
        dp_1[1] = 1
        for i in range(2, n+1):
            dp_0[i] = dp_0[i-1] + dp_0[i-2]
            dp_1[i] = dp_1[i-1] + dp_1[i-2]
        # print(dp_0, dp_1)
        print(dp_0[-1], dp_1[-1])