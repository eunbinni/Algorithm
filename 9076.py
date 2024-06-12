import sys

n = int(input())
        
# for _ in range(n):
#     array = list(map(int, input().split()))
#     array.remove(max(array))
#     array.remove(min(array))
#     if (max(array) - min(array)) >=4:
#         print('KIN')
#     else:
#         print(sum(array))
        
for _ in range(n):
    array = list(map(int, input().split()))
    array.sort()
    array.pop(4)
    array.pop(0)
    if (max(array) - min(array)) >=4:
        print('KIN')
    else:
        print(sum(array))