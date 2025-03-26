import sys
input = sys.stdin.readline
m = int(input())
s = set()

for _ in range(m):
    cal = input().strip()
    if cal.startswith("add"):
        _, x = cal.split()
        x = int(x)
        if x not in s:
            s.add(x)
    elif cal.startswith("remove"):
        _, x = cal.split()
        x = int(x)
        if x in s:
            s.remove(x)
    elif cal.startswith("check"):
        _, x = cal.split()
        x = int(x)
        if x in s:
            print(1)
        else:
            print(0)
    elif cal.startswith("toggle"):
        _, x = cal.split()
        x = int(x)
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif cal == "all":
        s = set(range(1, 21))
    elif cal == "empty":
        s = set()