# 첫째 줄에 큐브를 돌린 횟수 n이 주어진다. (1 ≤ n ≤ 1000)
# 둘째 줄에는 큐브를 돌린 방법이 주어진다. 각 방법은 공백으로 구분되어져 있으며, 
# 윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색
# 첫 번째 문자는 돌린 면이다. U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면이다. 
# 두 번째 문자는 돌린 방향이다. +인 경우에는 시계 방향 (그 면을 바라봤을 때가 기준), -인 경우에는 반시계 방향이다.

# U w
# D y
# F r
# B o
# L g
# R b

def initailized_variable():

    cube = {
        'U' : [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
        'D' : [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
        'F' : [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
        'B' : [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
        'L' : [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        'R' : [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    }

    arounds = {
        'face_U' : [(0, 0), (0, 1), (0, 2)],
        'face_R' : [(0, 2), (1, 2), (2, 2)],
        'face_D' : [(2, 2), (2, 1), (2, 0)],
        'face_L' : [(2, 0), (1, 0), (0, 0)]
    }
    targets = {
        'U' : [('B', 'face_U'), ('R', 'face_U'), ('F', 'face_U'), ('L', 'face_U')],
        'D' : [('F', 'face_D'), ('R', 'face_D'), ('B', 'face_D'), ('L', 'face_D')],
        'F' : [('U', 'face_D'), ('R', 'face_L'), ('D', 'face_U'), ('L', 'face_R')],
        'B' : [('U', 'face_U'), ('L', 'face_L'), ('D', 'face_D'), ('R', 'face_R')],
        'L' : [('U', 'face_L'), ('F', 'face_L'), ('D', 'face_L'), ('B', 'face_R')],
        'R' : [('U', 'face_R'), ('B', 'face_L'), ('D', 'face_R'), ('F', 'face_R')]
    }

    return cube, arounds, targets

def face_rot(cube,  key):
    face = cube[key]
    # i, j tuple
    # 0 0 / 0 1 / 0 2
    # 1 0 / 1 1 / 1 2
    # 2 0 / 2 1 / 2 2

    # rotation convert
    
    # 2 0 / 2 1 / 2 2
    # 1 0 / 1 1 / 1 2    
    # 0 0 / 0 1 / 0 2

    # 2-dimension list deep copy
    tmp = [[i for i in row] for row in face]    
    for i in range(3):
        index = 2
        for j in range(3):
            face[i][j] = tmp[index][i]
            # print('(', i,',  ', j, ')','              ', '(',index, ',  ', i, ')')
            index -= 1

def face_around_rot(cube, key, arounds, target):
    # B -> R -> F -> L 
    queue = [i for i in target]
    record = list()

    # queue is element = target face and line
    for element in queue:
        arr = cube[element[0]]
        for index in arounds[element[1]]:
            record.append(arr[index[0]][index[1]])

    # R -> F -> L -> B
    tmp = queue.pop(0)
    queue.append(tmp)

    while(queue):
        element = queue.pop(0)
        face = cube[element[0]]
        for index in arounds[element[1]]:
            face[index[0]][index[1]] = record.pop(0)
    
if __name__ == "__main__":
    inputs = list()

    for i in range(int(input())):
        garbage = int(input()) # ? 필요없는 압력인거같은데...
        arr = list(map(str, input().split()))
        inputs.append(arr)

    for arr in inputs:
        cube, arounds, targets = initailized_variable()
        for val in arr:
            key, isRight = val[0:1], val[1:2]
            loop = 1 if isRight == '+' else 3
            for i in range(loop):
                face_rot(cube, key)
                face_around_rot(cube, key, arounds, targets[key])

        for prt in cube['U']:
            result = prt[0]+prt[1]+prt[2]
            print(result)


# 4
# 1
# L-
# 2
# F+ B+
# 4
# U- D- L+ R+
# 10
# L- U- L+ U- L- U- U- L+ U+ U+

# rww
# rww
# rww

# bbb
# www
# ggg

# gwg
# owr
# bwb

# gwo
# www
# rww

# 1
# 6
# F+ R+ U+ B+ L+ D+