# 3
# 2 2 2
# 4 4 4
# 8 8 8

# 이동 가능 횟수 5
# 1 move 
# 4  2  0          
# 8  4  0 
# 16 8  0

# 4
# 2  4  16  8
# 8  4  0   0
# 16 8  2   0
# 2  8  2   0

# up, down, right, left
movable = [
    (1,0), (-1,0), (0,1), (0,-1)
]

# 4
# 1 1 0 4
# 1 1 0 1
# 2 2 4 2
# 0 0 2 0 
def move(arr, direction, length):
    # arr deep copy
    result = [[0 for _ in range(length)] for _ in range(length)]

    # if direction is up, ouput
    # 2 2 4 4
    # 2 2 2 1
    # 0 0 0 2
    # 0 0 0 0
    if direction == 0:
        board = [[arr[col][row] for col in range(length)] for row in range(length)]
        row = 0
        for queue in board:
            tmp = shift(queue, length)
            for col in range(length):
                result[row][col] = tmp.pop(0) 
            row += 1

    # if directio is down, ouput
    # 0 0 0 0
    # 0 0 0 4
    # 2 2 4 1
    # 2 2 2 2
    elif direction == 1:
        board = [[arr[col][row] for col in range(length-1, -1, -1)] for row in range(length)]
        print("if case is down :: ", board)
        for queue in board:
            tmp = shift(queue, length)
            print("shift queue :: " , tmp)

def shift(queue, size):
    result = list()
    while(queue):
        element = queue.pop(0)
        if element != 0:
            tmp = queue.pop(0)
            if element == tmp: result.append(element * 2)
            else :
                result.append(element)
                result.append(tmp)

    r_size = len(result)
    for _ in range(size-r_size): result.append(0)

    return result

if __name__ == "__main__":
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(number)]

    move(arr, 1, number)

# 알고리즘 숙련도
# python 2달
# spring - java 
# 빅데이터 머신러닝 핫하긴한데, 인력 -> 석.박사 
# 웹 앱 , 클라이언트
# 앱 - ios / java
# andoid -> java -> Kotlin -> Rxjava 
# Java : 선호하는 언어가 바껴서,
# 1주일 1번 4개월 -> 2개월 
# web : c / c++ 선헹, 과제 1주일 pointer 
# crud create read update delete

# print/ scan_f
# 분기, if / switch , for / while / do_while
# array
# strcture, class
# overwrite, overloading
# ptr
# ptr (linked list) 
# file read, write 
