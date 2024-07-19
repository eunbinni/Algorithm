def solution(s):
    answer = []
    d = []
    for string in s:
        if string in d:
            idx = [i for i, x in enumerate(d) if x == string]
            answer.append(len(d) - max(idx))
            d.append(string)
        else:
            d.append(string)
            answer.append(-1)
    return answer

print(solution(banana)) #[-1, -1, -1, 2, 2, 2]
print(solution(foobar)) #[-1, -1, 1, -1, -1, -1]