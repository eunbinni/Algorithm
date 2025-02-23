from collections import deque
t = int(input())

for _ in range(t):
    ps = input()
    stack = []

    for p in ps:
        if p == "(":
            stack.append(p)
        else: # ")"
            if stack:
                stack.pop()
            else:
                stack.append(")")
                break
    if stack:
        print("NO")
    else:
        print("YES")