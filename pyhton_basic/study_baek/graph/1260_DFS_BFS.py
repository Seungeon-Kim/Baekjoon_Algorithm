# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 1 2 4 3
# 1 2 3 4

# 0 1 1 1 
# 1 0 0 1
# 1 0 0 1
# 1 1 1 0

def start_dfs(arr, start, size):
    stack = list()
    stack.append(start-1)
    dfs(stack, arr, start-1, size)

def dfs(stack, arr, row, size):
    if len(stack) == size : 
        print("stack :: ", stack)
        return 
    print("now :: ", stack)

    for col in range(0, size):
        if arr[row][col] != 0 and row != col and col not in stack:
            stack.append(col)
            dfs(stack, arr, col, size)
    stack.pop()

def start_bfs(arr, start, size):
    queue = list()
    bfs(queue, arr, start-1, size)

def bfs(queue, arr, row, size):
    if size - 1 == row or row in queue: return

    queue.append(row)
    for col in range(0, size):
        if arr[row][col] != 0 and col not in queue:
            queue.append(col)

    print("queue :: " , queue)
    bfs(queue, arr, row+1, size)


if __name__ == "__main__":
    # 정점, 간선, 시작
    N, M, V = map(int, input().split())
    # N, M, V = 5, 4, 2

    arr = [[0] * N for i in range(N)]
    for i in range(M):
        k, j = map(int, input().split())
        k, j = k - 1, j -1
        arr[k][j] = 1
        arr[j][k] = 1

    print("arr :: " ,arr)

    start_dfs(arr, V, N)
    start_bfs(arr, V, N)