"""
def solution(arr):
    # stack
    # 연속 숫자 찾기, i번째랑 i+1이 같으면 연속처리, 거꾸로 시작
    for i in range(len(arr)-1, 0, -1):
        if arr[i] == arr[i-1]:
            arr.pop(i)
    return arr
"""
"""
효율성 탈락

del: 이 연산은 지정된 인덱스의 요소를 삭제하고, 리스트의 나머지 부분을 한 칸씩 앞으로 이동시켜 공간을 채움. 리스트 중간에 있는 요소를 삭제할 경우, 그 이후의 모든 요소를 메모리 상에서 한 칸씩 앞으로 이동시킴

pop(): 특정 인덱스의 요소를 삭제하고 그 요소를 반환함. 요소를 삭제한 후 리스트를 재조정해야 하므로, 특히 리스트 중간의 요소를 삭제할 때 비효율적
"""
def solution(arr):
    new_arr = []
    previous_num = None

    for num in arr:  # O(N)
        if num != previous_num:
            new_arr.append(num)
            previous_num = num

    return new_arr