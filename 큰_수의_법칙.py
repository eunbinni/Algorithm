n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr, reverse = True)
answer = []

while len(answer) != m:
    for _ in range(k):
        answer.append(arr[0])
        if len(answer) == m:
            break
    if len(answer) == m:
        break
    answer.append(arr[1]) # greedy

print(sum(answer))