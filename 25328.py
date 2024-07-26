import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

x = input().strip()
y = input().strip()
z = input().strip()
k = int(input())

com_list = []
com_list.extend(list(combinations(x,k)))
com_list.extend(list(combinations(y,k)))
com_list.extend(list(combinations(z,k)))
counter_list = Counter(com_list)
found = False
### 정렬 까먹고 안함, 정렬하기 위해서 다시 list에 담아둠 ###
result = []

for x in counter_list.items():
    if x[1] >= 2:
        result.append("".join(x[0]))
        found = True

result = sorted(result)
for answer in result:
    print(answer)

if not found:
    print(-1)
