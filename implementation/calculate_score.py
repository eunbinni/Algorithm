n = int(input())

lst = list(map(int, input().split()))
score = [0] * n
# 바로 전 값과 비교하기, 연속되는거니까
cnt = 1
for i in range(1, len(lst)):
    if lst[0] == 1: # 첫번째 인덱스 예외
        score[0] = 1

    if lst[i] == 1: # 맞은 경우
        if lst[i] == lst[i-1]:
            cnt += 1
            score[i] = cnt
        else:
            score[i] = 1
            cnt = 1
    else:
        pass

print(sum(score))