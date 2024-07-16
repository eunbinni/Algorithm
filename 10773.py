import sys

input = sys.stdin.readline
k = int(input())

num_list = [int(input()) for _ in range(k)]

stack = []

for num in num_list:
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)

print(sum(stack))