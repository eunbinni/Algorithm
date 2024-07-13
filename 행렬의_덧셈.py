"""
zip(arr1, arr2)의 사용법
인덱스가 같은 요소를 나눈 후 튜플로 묶어줌
출력해보려면 list(zip(arr1, arr2)
"""
def solution(arr1, arr2):
    answer = []
    for x,y in zip(arr1, arr2):
        row = []
        for a,b in zip(x,y):
            row.append(a+b)
        answer.append(row)

    return answer