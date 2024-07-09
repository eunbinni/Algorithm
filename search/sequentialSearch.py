import sys
input = sys.stdin.readline
def sequential_search(n, target, array):
    i = 0
    for i in range(int(n)):
        if array[i] == target:
            return i+1

n, input_data = input().split()

array = list(input().split())

print(sequential_search(n, input_data, array))