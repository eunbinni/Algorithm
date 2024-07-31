"""
string & stack & 구현
다시풀기 : 0회째
"""
import sys
from collections import deque

input = sys.stdin.readline
words = input()
stack = deque()
result = ""
flag = False

for s in words:
    if not flag: # 뒤집어야 하는 문자열인경우
        if s == " " or s == '\n':
            while stack:
                result += stack.pop()
            result += " "

        else:
            if s == "<": # 다음 < 가 나오게 되면
                # print(s)
                while stack:
                    result += stack.pop()
                flag = True
            stack.append(s)

    else:# <가 나온 경우, 그대로 출력해야함
        stack.append(s)
        if s == ">":
            while stack:
                result += stack.popleft()
            flag = False

print(result)

"""
테스트 케이스는 맞았지만 제출하면 틀린 코드
"""
# # 기호가 아예 없을 경우
# if start == -1:
#     special_list.extend(word_list.split())
# else:
# # # 기호가 있을 경우
#     while start != -1:
#         end = word_list.find('>', start + 1) # < 찾은 다음부터 ">" 찾기
#         special_list.append(word_list[start:end+1]) # <~~~>까지 list append
#         # print(special_list)
#         start = word_list.find('<', end+1) # end 다음부터 < 다시 찾기
#         if start != -1:
#             special_list.append(word_list[end + 1:start])
#         else:
#             special_list.append(word_list[end+1:])
#             break
#
# result = ""
#
# for i, word in enumerate(special_list):
#     if word.startswith('<'):
#         result += word
#     else:
#         # char_list = list(word)
#         # while char_list:
#         #     result += char_list.pop()
#         result += word[::-1]
#         # print(i, result)
#         if i < len(special_list) - 1 and not special_list[i+1].startswith('<'):
#             result += " "
#
# print(result)