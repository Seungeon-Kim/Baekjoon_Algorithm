# 3 4 5
# 3 2
# 2 2
# 3 1
# 2 3
# 1 1

# 4

movable = [(1,0), (-1,0), (0,1), (0,-1)]

def initailized_matrix(row, col, arr):
    matrix = [[[0, 0] for _ in range(col)] for _ in range(row)]

    for garbage in arr:
        # is move
        matrix[garbage[0]-1][garbage[1]-1][0] = 1  
        # checked move
        matrix[garbage[0]-1][garbage[1]-1][1] = 0  

    return matrix

#  # . . .
#  . # # .
#  # # . .

def search_dfs(mat, row, col, start):
    matrix = [[[val for val in mat[i][j]] for j in range(col)] for i in range(row)]
    # x, y, size
    stack = [(start[0]-1, start[1]-1, 1)]
    matrix[start[0]-1][start[1]-1][1] = 1
    biggest = 0

    while stack:
        frame = stack.pop(0)
        for move in movable:
            x, y = frame[0] + move[0], frame[1] + move[1]
            if 0 <= x < row and 0 <= y < col and matrix[x][y][0] == 1 and matrix[x][y][1] == 0:
                matrix[x][y][1] = 1
                block = (x, y, frame[2] + 1)
                biggest = max(biggest, block[2])
                stack.append(block)

    return biggest

if __name__ == "__main__":
    row, col, number = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(number)]
    biggest = 0

    mat = initailized_matrix(row, col, arr)
    for start in arr:
        biggest = max(biggest, search_dfs(mat, row, col, start))
        # print(start[0], "   ", start[1])
        # print("biggest :: ", search(mat, row, col, start))
    print(biggest)

