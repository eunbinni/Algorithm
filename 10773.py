import sys

input = sys.stdin.readline
data = input().split()
k = int(data[0])
num_list = list(map(int, data[1:]))

stack = []

for num in num_list:
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)

print(sum(stack))