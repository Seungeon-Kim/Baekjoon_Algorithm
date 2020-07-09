# 상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다.
# ㅁ  ㅁ - ㅁ
# 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.

# 상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.

# [input]
# 6
# 5
# 1 2
# 1 3
# 3 4
# 2 3
# 4 5
# [output]
# 3

# 0 1
# 0 2
# 2 3 
# 1 2 
# 3 4

def initialized_matrix(arr, size):
    # 0 1 1 0 0 0
    # 1 0 1 0 0 0
    # 1 1 0 1 0 0
    # 0 0 1 0 1 0
    # 0 0 0 1 0 0
    # 0 0 0 0 0 0 
    result = [[0 for _ in range(size)] for _ in range(size)]
    for pair in arr:
        x, y = pair[0]-1, pair[1]-1
        result[x][y] = 1
        result[y][x] = 1
    
    return result

def start_dfs(start, mat, size):
    friends = [start]
    queue = [start]
    loop = 0

    while queue:
        element = queue.pop(0)
        for index in range(size):
            if loop == 0 and mat[element][index] == 1:
                friends.append(index)
                queue.append(index)
            elif mat[element][index] == 1:
                friends.append(index)
        loop += 1
    
    return friends

if __name__ == "__main__":
    node_size = int(input())
    link_size = int(input())
    pair_arr = [list(map(int, input().split())) for _ in range(link_size)]
    
    matrix = initialized_matrix(pair_arr, node_size)
    friends = start_dfs(0, matrix, node_size)
    print(len(set(friends))-1)

