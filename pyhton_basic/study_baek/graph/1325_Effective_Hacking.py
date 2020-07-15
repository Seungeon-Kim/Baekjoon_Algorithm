import sys
from collections import deque

def initailized_matrix(row, col, links):
    matrix = [[0 for _ in range(row)] for _ in range(row)]

    for link in links:
        matrix[link[1]-1][link[0]-1] = 1
    return matrix

def bfs(matrix, length, start):
    queue = deque()
    frame = (start, 0)
    queue.append(frame)
    result = 0

    while queue:
        frame = queue.popleft()
        i = frame[0]
        result = max(result, frame[1])
        for j in range(length):
            if matrix[i][j] == 1:
                element = (j, frame[1] + 1)
                queue.append(element)

    return (start, result)
            


if __name__ == "__main__":
    row, col = map(int, sys.stdin.readline().split())
    links = [list(map(int, sys.stdin.readline().split())) for _ in range(col)]
    matrix = initailized_matrix(row, col, links)
    
    temp = list()
    for start in range(col):
        temp.append(bfs(matrix, col, start))

    max_value = 0
    result = list()
    for tmp in temp:
        if max_value < tmp[1]:
            result = [tmp[0]+1]
            max_value = tmp[1]
        elif max_value == tmp[1]:
            result.append(tmp[0]+1)
        
    result.sort()
    for ptr in result:
        print(str(ptr), end=' ')