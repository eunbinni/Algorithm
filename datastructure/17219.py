n, m = map(int, input().split())

dic = {}
for _ in range(n):
    site, password = input().split()
    dic[site] = password

for _ in range(m):
    x = input()
    print(dic[x])