def solution(ingredient):
    answer = 0
    stack = []
    hamburger = [1, 2, 3, 1]

    for item in ingredient:
        stack.append(item)
        if len(stack) >= 4 and stack[-4:] == hamburger:
            answer += 1
            del stack[-4:]
    return answer
print([2, 1, 1, 2, 3, 1, 2, 3, 1]) # 2
print([1, 3, 2, 1, 2, 1, 3, 1, 2]) # 0

# 시간 초과 코드
"""
def solution(ingredient):
    answer = 0
    ham_list = []
    hamburger = [1, 2, 3, 1]
    
    for item in ingredient:
        ham_list.append(item)
        if ham_list[-4:] == hamburger:
            answer += 1
            ham_list = ham_list[:-4]
    
    return answer
"""
