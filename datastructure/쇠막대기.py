a = input()
lst = [x for x in a]
stack = []
sumv = 0
for i in range(len(lst)):
    if lst[i] == "(":
        # lst.pop()
        stack.append(lst[i])
    else: # )
        if lst[i-1] == '(':
            stack.pop()
            sumv += len(stack)
        else:
            stack.pop()
            sumv += 1
print(sumv)
# (((()())(())()))