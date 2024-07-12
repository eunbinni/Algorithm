def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost) # 여벌 체육복을 가진 학생이 도난당할 수도 있음
    set_lost = set(lost) - set(reserve)

    for student in set_reserve:
        if student - 1 in set_lost:
            set_lost.remove(student - 1)
        elif student + 1 in set_lost:
            set_lost.remove(student + 1)
    # print(set_lost)

    answer = n - len(set_lost)

    return answer