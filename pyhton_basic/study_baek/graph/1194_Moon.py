# 빈 곳 : 언제나 이동할 수 있다. ('.‘로 표시됨)
# 벽 : 절대 이동할 수 없다. (‘#’)
# 열쇠 : 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. (a - f)
# 문 : 대응하는 열쇠가 있을 때만 이동할 수 있다. (A - F)
# 민식이의 현재 위치 : 빈 곳이고, 민식이가 현재 서 있는 곳이다. (숫자 0)
# 출구 : 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. (숫자 1)
# 달이 차오르는 기회를 놓치지 않기 위해서, 미로를 탈출하려고 한다. 한 번의 움직임은 현재 위치에서 수평이나 수직으로 한 칸 이동하는 것이다.

# 민식이가 미로를 탈출하는데 걸리는 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 7 8
# a#c#eF.1
# .#.#.#..
# .#B#D###
# 0....F.1
# C#E#A###
# .#.#.#..
# d#f#bF.1



import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
dist = [[[0]*64 for _ in range(m)] for _ in range(n)]
q = deque()

def init():
    for i in range(n):
        for j in range(m):
            if a[i][j] == '0':
                q.append((i, j, 0))
                return

def bfs():
    while q:
        x, y, k = q.popleft()
        if a[x][y] == '1':
            print(dist[x][y][k])
            return
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny, nk = x+dx, y+dy, k
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            c = a[nx][ny]
            if c.islower():
                nk |= (1<<(ord(c)-ord('a')))
            elif c.isupper() and not nk & (1<<(ord(c)-ord('A'))):
                continue
            if not dist[nx][ny][nk] and c != '#':
                q.append((nx, ny, nk))
                dist[nx][ny][nk] = dist[x][y][k] + 1
    print(-1)
if __name__ == "__main__":    
    init()
    print(dist)

    bfs()