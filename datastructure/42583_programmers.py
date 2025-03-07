# 다리를 지나는 트럭 https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cur_bridge = [0] * bridge_length
    cur_weight = 0
    truck_weights = deque(truck_weights)
    cur_bridge = deque(cur_bridge)
    while len(truck_weights) > 0:
        answer += 1
        cur_weight = cur_weight - cur_bridge.popleft()
        if cur_weight + truck_weights[0] <= weight:
            p = truck_weights.popleft()
            cur_weight += p
            cur_bridge.append(p)
        else:
            print(answer, cur_bridge)
            cur_bridge.append(0)
        # print(answer, cur_bridge, truck_weights)
    answer += bridge_length
    return answer