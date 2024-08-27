import heapq

def solution(scoville, K):
    answer = 0
    """
    1. 스코빌 리스트 sort -> heapq로 구현
    2. 스코빌 지수가 낮은 두가지 원소 추출
    3. scoville list의 원소들이 전부 >= k ?????
    4. 아니라면, 두가지 원소를 섞어서 스코빌 지수 계산, 섞을때마다 answer +=1
    5. 섞은 음식의 스코빌 지수를 scoville list에 append
    """
    heapq.heapify(scoville)
    
    while scoville:
        result1 = heapq.heappop(scoville)
        if result1 >= K:
            break
        else:
            if not scoville:
                return -1
            else:
                result2 = heapq.heappop(scoville)
                sc_score = result1 + (result2 * 2)
                heapq.heappush(scoville, sc_score)
                answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2