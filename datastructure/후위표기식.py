from collections import deque
s = input()
# lst = []
stack = []
answer = []
# queue = deque()

for x in s:
    if x.isdigit():
        answer.append(x)
    elif x == "(":
        stack.append(x)
    elif x == ")":
        while stack and stack[-1] != "(":
            answer.append(stack.pop())
        stack.pop() # ( 제거
    elif x == "*" or x == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"): # 왼쪽에 있다는 얘기
            p = stack.pop()
            answer.append(p)
        stack.append(x)
    elif x == "+" or x == "-":
        while stack and stack[-1] != "(":
            p = stack.pop()
            answer.append(p)
        stack.append(x)

while stack:
    p = stack.pop()
    answer.append(p)

string = ''.join(answer)

stack = []
for s in string:
    if s.isdigit():
        stack.append(int(s))
    elif s == '*':
        p = stack.pop()
        q = stack.pop()
        stack.append(p*q)
    elif s == '-':
        p = stack.pop()
        q = stack.pop()
        stack.append(q-p)
    elif s == '/':
        p = stack.pop()
        q = stack.pop()
        stack.append(q/p)
    elif s == '+':
        p = stack.pop()
        q = stack.pop()
        stack.append(q+p)
    # print(stack)
print(int(stack[0]))