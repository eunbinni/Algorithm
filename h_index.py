def solution(citations):
    h_list = []
    sorted_cit = sorted(citations)
    cit_max = max(citations)
    for h in range(cit_max):
        cnt = 0
        for cit in sorted_cit:
            if h <= cit:
                cnt += 1
            if cnt >= h:
                h_list.append(h)
    return max(h_list) if h_list else 0

print(solution([3, 4])) # 2
print(solution([1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 6])) # 5