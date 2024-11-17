from collections import deque

def solution(s):
    answer = True
    queue = deque()
    for bracket in s:
        if len(queue) >= 1:
            if bracket == ")":
                prev_bracket = queue.popleft()
            else: # "("
                queue.append(bracket)
        else:
            queue.append(bracket)
            
    if len(queue) != 0:
        return False
    
    return True
solution("()()") # true
solution("(())()") # true
solution(")()(") # false
solution("(()(") # false