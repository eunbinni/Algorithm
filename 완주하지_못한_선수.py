from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant) # Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
    completion_count = Counter(completion) # Counter({'stanko': 1, 'ana': 1, 'mislav': 1})

    for name in participant:  # 참여자 명단을 돌면서
        if participant_count[name] > completion_count[name]: # 개수가 더 많으면
            return name # 그 이름 리턴