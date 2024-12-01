def solution(numbers, target):
    answer = 0
    num_list = [0]
    for num in numbers: # num = 1, num_list = [4, -4]
        tmp = []
        for i in num_list: # i = 0
            tmp.append(i + num) # tmp = [4]
            tmp.append(i - num) # tmp = [4, -4]
        num_list = tmp
    for num in num_list:
        if num == target:
            answer += 1
    
    return answer