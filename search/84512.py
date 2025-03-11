# 프로그래머스 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

alpha = ["A", "E", "I", "O", "U"]
cnt = 0
# word = "AAAAE"
word = "I"
s = ''
answer = -1

def dfs(cnt, s, word):
    # 종료 조건
    global answer
    if cnt <= 5:
        answer += 1
        # print(s, answer)
        if s == word:
            print(answer)
    else:
        return
    for i in range(5):
        dfs(cnt+1, s + alpha[i], word)

print(dfs(0, '', word))