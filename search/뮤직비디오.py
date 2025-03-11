# 30으로 했을 때 1장에 다 담기면,3장에도 담기는거 잊지않기
n, m = map(int, input().split())
lst = list(map(int, input().split()))
# lst.sort()

start = max(lst) # 0이 아닌 이유는 최소 길이가 하나는 담아야 하기 때문
end = sum(lst) # 모든 곡을 한장에 담아야 함
result = end # 아무것도 탐색 못할까봐

while start <= end:
    sumv = 0
    mid = (start + end) // 2
    cnt = 1
    for x in lst:
        if sumv + x > mid: # 추가할 수 없음. 넘침
            cnt += 1 # 새로운 dvd 사용 횟수 추가
            sumv = x
        else: # 담을 수 있는 경우
            sumv += x

    if cnt <= m: # 더 줄일 수 있는 상황
        result = mid
        end = mid-1
    else:
        start = mid + 1

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    sumv = 0
    for i in range(len(lst)-1):
        sumv = sumv + lst[i]
        if sumv+lst[i+1] > mid:
            sumv = 0
            cnt += 1
    if cnt <= m: # 더 줄일 수 있는 상황
        end = mid-1
        result = mid
    else:
        start = mid + 1
print(result)