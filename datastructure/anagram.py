string1 = input()
string2 = input()

## 1
dict_1 = {}
dict_2 = {}

for s in string1:
    if s not in dict_1:
        dict_1[s] = 0
    else:
        dict_1[s] += 1

for s in string2:
    if s not in dict_2:
        dict_2[s] = 0
    else:
        dict_2[s] += 1

## 2
from collections import defaultdict

dict_1 = defaultdict(int)
dict_2 = defaultdict(int)

## 2
for s in string1:
    dict_1[s] += 1

for s in string2:
    dict_2[s] += 1

## 3
from collections import Counter

dict_1 = Counter(string1)
dict_2 = Counter(string2)
#
if dict_1 == dict_2:
    print('YES')
else:
    print('NO')

## 4
dic = {}
for s in string1:
    dic[s] = dic.get(s, 0)+1

for s in string2:
    dic[s] = dic.get(s, 0)-1

if all(cnt == 0 for value, cnt in dic.items()):
    print('YES')
else:
    print('NO')