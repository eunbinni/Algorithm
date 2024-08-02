"""
브 2, 다시 풀지 않음
"""
a, b = input().split()
# a와 b를 string으로 받는다
# a를 string 하나씩 자른다
# 항상 세자리 수다
A = int(a[2] + a[1] + a[0])
B = int(b[2] + b[1] + b[0])

if A > B:
    print(A)
else:
    print(B)