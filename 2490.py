import sys
input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(3)]
# matrix = [list(map(int, input().split())) for _ in range(3)] # sys.stdin과 시간 같음

for row in matrix:
    if row.count(0) == 1: 
        print("A")
    elif row.count(0) == 2: 
        print("B")
    elif row.count(0) == 3: 
        print("C")
    elif row.count(0) == 4: 
        print("D")
    else: 
        print("E")