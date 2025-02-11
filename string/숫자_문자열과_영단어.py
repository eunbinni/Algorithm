def solution(s):
    answer = ""
    temp = ""
    
    digit_play = {"zero" : "0",
    "one" : "1",
    "two" : "2", 
    "three" : "3",
    "four" : "4", 
    "five" : "5", 
    "six" : "6",
    "seven" : "7", 
    "eight" : "8", 
    "nine" : "9"}
    
    if s.isdigit():
        return int(s)
    
    for string in s:
        if string.isdigit():
            answer += string
        else: # 문자
            temp += string
        if temp in digit_play.keys():
            answer += digit_play[temp]
            temp = ""
    return int(answer)