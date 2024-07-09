import sys

input = sys.stdin.readline
n, m = map(int, input().split())

listen = []
for _ in range(n):
    listen.append(input().strip())

see = []
for _ in range(m):
    see.append(input().strip())

"""
시간초과 바보아님? 왜 for문을 두번 쓰려고해
"""
# count = 0
# for listen_name in listen:
#     if listen_name in see:
#         count += 1
# print(count)
#
# for listen_name in listen:
#     if listen_name in see:
#         print(listen_name)
name_list = sorted(set(listen) & set(see))
print(len(name_list))
for name in name_list:
    print(name)
