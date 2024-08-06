def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p)+1):
        sub = []
        for j in range(len(p)):
            sub.append(t[i + j])
        t_sub = ''.join(sub)
        print(t_sub)
        if int(t_sub) <= int(p):
            answer += 1

    return answer

print(solution("3141592", "271")) # 2
print(solution("500220839878", "7")) # 8
print(solution("10203", "15")) # 3