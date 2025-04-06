n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
blue_cnt, white_cnt = 0, 0

"""
n, n/2, n/4 씩 나누어서 재귀 돌리기
값과 같은지 확인하는 flag 변수 
"""

def recur(n, y, x):
    global blue_cnt, white_cnt

    same_flag = True
    color = matrix[y][x] # 현재 좌표 색 정보
    ny = y + n
    nx = x + n
    for j in range(y, ny):
        for i in range(x, nx):
            if matrix[j][i] != color:
                same_flag = False
                break

    if not same_flag: # 다르면 계속 탐색
        k = n // 2
        recur(k, y, x)
        recur(k, y+k, x)
        recur(k, y, x+k)
        recur(k, y+k, x+k)
    else:
        if color == 1: # blue
            blue_cnt += 1
        elif color == 0: # white
            white_cnt += 1

recur(n, 0, 0)
print(white_cnt)
print(blue_cnt)