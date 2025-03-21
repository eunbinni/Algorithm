# 프로그래머스 그리디 lv3
"""
1. sort를 생각해냈지만 x[0]로 시도함, 하지만 나가는 지점에 설치해야되기 때문에 x[1] 기준 정렬
2. 왜 그리디인가? 설치 가능한 지점을 전부 탐색하면서 cnt를 늘려나가기 때문
3. 현재 cam으로 커버가 가능하면 i를 증가시키면서 다음꺼 탐색하면 됨
4. cam으로 커버 불가능하면 거기에 설치해야 된다는 의미이기 때문에 그 나가는 지점을 새로운 cam으로 두고 cnt 증가

"""
def solution(routes):
    routes = sorted(routes, key = lambda x:x[1])
    cnt = 0
    i = 0
    while i < len(routes):
        cam = routes[i][1]
        cnt += 1
        while i < len(routes) and cam >= routes[i][0]:
            i += 1
    return cnt