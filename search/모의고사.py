def exhaustive_search(answers, math_fail):
    score = 0
    for i in range(len(answers)):
        if len(math_fail) < len(answers):
            math_fail = math_fail * (len(answers) - len(math_fail))
        if math_fail[i] == answers[i]:
            score += 1
    return score

def solution(answers):
    final = []
    score_list = {}
    one = [1,2,3,4,5]
    two = [2,1, 2,3, 2,4, 2,5]
    three = [3,3, 1,1, 2,2, 4,4, 5,5]
    score_list[1] = exhaustive_search(answers, one)
    score_list[2] = exhaustive_search(answers, two)
    score_list[3] = exhaustive_search(answers, three)
    max_score = max(score_list.values())
    for key, score in score_list.items(): ## 생각못함
        if score == max_score:
            final.append(key)
    
    return sorted(final)