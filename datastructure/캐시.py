# 프로그래머스

from collections import deque
"""
1. LRU 알고리즘에서 주의할 점: cache hit 한 값은 큐에서 remove 하고 큐의 뒤로 들어와야 한다.
2. cacheSize가 cities보다 큰 경우 고려하지 못함
"""
def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    cities = deque(cities)
    if cacheSize == 0:
        return 5 * len(cities)

    while cities:
        city = cities.popleft()
        city = city.lower()
        if city in queue:
            answer += 1
            queue.remove(city)
            queue.append(city)
        else:
            answer += 5
            if len(queue) < cacheSize:
                queue.append(city)
            else:
                queue.popleft()
                queue.append(city)
    return answer

