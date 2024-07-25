def solution(s):
    answer = 0
    
    cnt1 = 0
    cnt2 = 0
    x = s[0]
    for i in s:
        if cnt1 == cnt2:
            answer += 1
            k = i # b 저장
        if k == i:
            cnt1 +=1 # 첫글자와 같을 때
        else:
            cnt2 +=1
    
    return answer
print(solution("banana")) #3
print(solution("abracadabra")) #6
print(solution("aaabbaccccabba")) #3