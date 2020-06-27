
# 3 4
# 1 1
# 1 3
# 2 2
# 3 2

# 2


# 3 5
# 1 1
# 1 3
# 2 2
# 3 2
# 3 1

# 2


# 5 7
# 1 2
# 2 2
# 2 5
# 3 4
# 4 4 
# 5 1
# 5 3

# 4
def dp(arr, n , k):
    row_flag = False
    col_flag = False
    now_flag = False
    cnt = 0 

    # 0 // 1 2
    # 1 // 2
    # 2 // 
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i][i] == 1 : now_flag = True
            if arr[i][j] == 1 : row_flag = True
            if arr[j][i] == 1 : col_flag = True


        if row_flag == False and col_flag == False and now_flag == True :
            cnt += 1
        else :
            if row_flag :
                cnt += 1
            if col_flag :
                cnt += 1
        
        now_flag = False
        col_flag = False
        row_flag = False

    return cnt


if __name__ == "__main__":
    n, k = map(int, input().split())

    arr = [[0] * n for i in range(n)]

    for i in range(k):
        row, col = map(int, input().split())
        arr[row-1][col-1] = 1

    print(dp(arr, n, k))