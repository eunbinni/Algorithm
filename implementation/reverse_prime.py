n = int(input())
lst = list(map(int, input().split()))

def reverse(x):
    x = str(x)
    return int(x[::-1])
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0: # 나누어 떨어짐, 소수 아님
            return False
    return True

for num in lst:
    num = reverse(num)
    if isPrime(num):
        print(num, end = ' ')