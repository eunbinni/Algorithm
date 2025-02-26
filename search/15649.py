N, M = map(int, input().split())
ans = []
visited = [False] * (N+1)

def back():
    if len(ans) == M:  # 배열의 길이를 확인
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N + 1):  # 1 ~ N 까지
        if not visited[i]:
            ans.append(i)  # 배열 추가
            visited[i] = True
            back()  # 재귀
            ans.pop()  #  return으로 돌아오면 이게 실행됨. 1, 2, 3 일때 3을 없앰으로 전 단계로 돌아가는 것
            visited[i] = False

back()