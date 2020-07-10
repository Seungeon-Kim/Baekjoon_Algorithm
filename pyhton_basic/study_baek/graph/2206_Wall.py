from collections import deque
movalbe = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(arr, row, col):
    #row, col, isCrash, count
    queue = deque()
    queue.appendleft((0, 0, 0, 1)) 
    goal = (row-1, col-1)

    while queue:
        now = queue.popleft()
        if now[0] == goal[0] and now[1] == goal[1]: return now[3]

        for move in movalbe:
            position = (now[0] + move[0], now[1] + move[1], now[2], now[3])

            if 0 <= position[0] < row and 0 <= position[1] < col:
                #movalbe
                if arr[position[0]][position[1]] == 0:
                    position = (position[0], position[1], position[2], position[3]+1)
                    queue.append(position)
                elif arr[position[0]][position[1]] == 1 and position[2] == 0:
                    position = (position[0], position[1], 1, position[3]+1)
                    queue.append(position)
                else:
                    pass
            else:
                #not movable
                pass
        
    return -1

if __name__ == "__main__":
    row, col = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(row)]


    print(bfs(arr, row, col))



# 6 4
# 0110
# 0110
# 0000
# 0000
# 1111
# 0000