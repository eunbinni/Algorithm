"""
프로그래머스 추억점수
"""
def solution(name, yearning, photo):
    answer = []

    # 딕셔너리 만들기
    think_idx = {}
    for i in range(len(name)):
        think_idx[name[i]] = yearning[i]

    for row in photo:
        cnt = 0
        for person in row:
            if person in name:
                cnt += think_idx[person]
            else:
                pass
        answer.append(cnt)

    return answer