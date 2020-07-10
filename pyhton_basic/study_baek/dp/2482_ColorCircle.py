
# 입력 파일의 첫째 줄에 색상환에 포함된 색의 개수를 나타내는 양의 정수 N(4≤N≤1,000)이 주어지고, 둘째 줄에 N색상환에서 선택할 색의 개수 K(1≤K≤N)가 주어진다. 

# color = 7, select = 2
# (7 ,2) = (6, 2) + (5, 1)
# (6 ,2) = (5, 2) + (4, 1)
# (5 ,2) = (4, 2) + (3, 1)
# (4 ,2) = (3, 2) + (2, 1)



# color = 7, select = 3
# (7 ,3) = (6, 3) + (5, 2)
# (6 ,3) = (5, 3) + (4, 2)
# (5 ,3) = (4, 3) + (3, 2)
# (4 ,3) = (3, 3) + (2, 2)

# 7 = 2 + 5
# 2 = 0 + 2
# 0 = 0 + 0
# 0 = 0 + 0 

# [n][m] = [n-1][m] + [n-2][m-1]
# n = color, m = select
#   m  1  2  3  4  5  6  7
# n
# 1    1 
# 2    2  0
# 3    3  0  0 
# 4    4  2  0  0
# 5    5  5  0  0  0
# 6    6  9  2  0  0  0 
# 7    7  14 7  0  0  0  0  0


def colors(color_size, select_num):
    arr = [[ 0 if i != 0 else j for i in range(j)] for j in range(color_size+1)]
    # color_size = 7, select_num = 2
    # [[], 
    # [1], 
    # [2, 0], 
    # [3, 0, 0], 
    # [4, 0, 0, 0], 
    # [5, 0, 0, 0, 0], 
    # [6, 0, 0, 0, 0, 0], 
    # [7, 0, 0, 0, 0, 0, 0]]
    if select_num == 1:
        return arr[color_size][0]
    else:  
        for i in range(4, color_size+1):
            for j in range(1, i-1):
                arr[i][j] = arr[i-1][j] + arr[i-2][j-1]

        return arr[color_size][select_num-1]
   
    # [[], 
    # [1], 
    # [2, 0], 
    # [3, 0, 0], 
    # [4, 2, 0, 0], 
    # [5, 5, 0, 0, 0], 
    # [6, 9, 2, 0, 0, 0], 
    # [7, 14, 7, 0, 0, 0, 0]]


if __name__ == "__main__":
    color_size = int(input())
    select_num = int(input())

    get_num = colors(color_size, select_num)
    print(get_num % 1000000003)  