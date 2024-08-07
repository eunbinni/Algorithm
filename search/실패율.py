def solution(N, stages):
    answer = []
    fail = {}
    cnt = {}
    # n번 스테이지의 실패율 분자 계산하기
    for num in stages:
        if num not in cnt:
            cnt[num] = 1
        else:
            cnt[num] += 1
    # print(cnt)

    # 실패율 계산하기
    remain_players = len(stages)  # player를 단계마다 빼기

    for i in range(1, N + 1):
        if i in cnt.keys():
            fail[i] = cnt[i] / remain_players
            remain_players = remain_players - cnt[i]
        else:
            fail[i] = 0
    # print(fail)

    fail_sorted = sorted(fail.items(), reverse=True, key=lambda x: x[1])
    for idx in fail_sorted:
        answer.append(idx[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]