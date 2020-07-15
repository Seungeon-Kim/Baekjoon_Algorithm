import sys
from collections import deque

def bfs(mat, length, i , j):
    matrix = [[i for i in arr] for arr in mat]
    visited = set()
    queue = deque()
    if i == j :
        for k in range(length):
            if matrix[i][k] == 1:
                queue.appendleft(k)
        # queue = [k if matrix[i][k] == 1 else  for k in range(length)]
    
    else: queue.appendleft(i)

    
    while queue:
        value = queue.popleft()
        if value == j: return 1
        for node_index in range(length):
            if matrix[value][node_index] == 1 and (value, node_index) not in visited:
                visited.add((value, node_index))
                queue.append(node_index)

    return 0


if __name__ == "__main__":
    number = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _  in range(number)]
    result = [[i for i in range(number)] for _ in range(number)]

    for i in range(number):
        for j in range(number):
            result[i][j] = bfs(matrix, number, i, j)

    for i in range(number):
        for j in range(number):
            print(result[i][j], end=' ')
        print("")


# 1 0 1 1 1 1 1
# 0 0 1 0 0 0 1
# 0 0 0 0 0 0 0
# 1 0 1 1 1 1 1
# 1 0 1 1 1 1 1
# 0 0 1 0 0 0 1
# 0 0 1 0 0 0 0

# [1, 0, 1, 1, 1, 1, 1]
# [0, 0, 1, 0, 0, 0, 1]
# [0, 0, 0, 0, 0, 0, 0]
# [1, 0, 1, 1, 1, 1, 1]
# [1, 0, 1, 1, 1, 1, 1]
# [0, 0, 1, 0, 0, 0, 1]
# [0, 0, 1, 0, 0, 0, 0]