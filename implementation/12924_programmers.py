# 숫자의 표현
# sum > n 조건 없으면 효율성 탈락 -> sum이 n을 넘으면 탐색할 필요 없기 때문에
def solution(n):
    answer = 0
    sum = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    return answer
print(solution(15)) # 4


#################
# 처음 풀었던 코드

"""
def solution(n):
    answer = 0
    cnt = 0
    lst = [i for i in range(1, n + 1)]
    for x in range(1, n + 1):
        for i in range(n):
            num = 0
            for _ in range(x):
                num += lst[i]
                print(x, i, num)
                if num == n:
                    cnt += 1
                    break

    return cnt
"""