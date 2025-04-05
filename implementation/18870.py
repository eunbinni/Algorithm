n = int(input())

lst = list(map(int, input().split()))

set = set(lst)
set_lst = list(set)
set_lst.sort()
from collections import defaultdict
dic = defaultdict(int)
for idx, value in enumerate(set_lst):
    dic[value] = idx
# print(dic)

for x in lst:
    print(dic[x], end = ' ')
"""
lst.index(x)로 접근하면 O(n)이 걸려서 for문과 합치면 O(n^2)로 시간초과
dict 이용하여 O(1), 총 O(n)으로 변경
"""