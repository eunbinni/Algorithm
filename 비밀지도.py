def solution(n, arr1, arr2):
    answer = []
    # 10 to 2 bin()
    # 2 to 10 int(,2)
    two_arr1 = []
    two_arr2 = []
    for integer in arr1:
        row = str(bin(integer)[2:])
        if len(row) < n:
            row = row.zfill(n)
        two_arr1.append(row)
    for integer in arr2:
        row = str(bin(integer)[2:])
        if len(row) < n:
            row = row.zfill(n)
        two_arr2.append(row)
    final_row = ""
    for i in range(n):
        for j in range(n):
            if two_arr1[i][j] == "0" and two_arr2[i][j] == "0":
                final_row += " "
            if two_arr1[i][j] == "1" or two_arr2[i][j] == "1":
                final_row += "#"
        answer.append(final_row)
        final_row = ""
    
    return answer
solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])  # ["#####", "# # #", "### #", "#  ##", "#####"]
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]) # ["######", "###  #", "##  ##", " #### ", " #####", "### # "]