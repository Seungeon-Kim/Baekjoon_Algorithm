# 사람 수, 파티 수
# 4 3

# 진실을 아는 사람 수
# 0


# 4 3
# 0
# 2 1 2
# 1 3
# 3 2 3 4

# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0

# 0 1 0 0 
# 1 0 1 1 
# 0 1 0 1
# 0 1 1 0

# DFS로 참여하면 안되는 사람들 추출 (연결되는 놈들 다 거짓부렁이 판별사)
# 독립적인 노드만 참여하는 파티 갯수 세면 될 듯
def initailized_matrix(size, nodes):
    mat = [[0 for _ in range(size)] for _ in range(size)]
    for node in nodes:
        if node[0] != 0:
            for i in range(node[0] - 1) :
                for j in range(i+1, node[0]):
                    mat_i, mat_j = node[i+1]-1, node[j+1]-1
                    mat[mat_i][mat_j] = 1
                    mat[mat_j][mat_i] = 1

    return mat

# 0 1 0 0 
# 1 0 1 1 
# 0 1 0 1
# 0 1 1 0

# 2
def start_bfs(mat, start, size):
    visited = [start]
    queue = [start]

    while queue and len(visited) != size:
        parent = queue.pop(0)
        for index in range(size):
            child = mat[parent][index]
            if child == 1 and index not in visited:
                queue.append(index)
                visited.append(index)

    return visited 

def get_num_party(parties, can):
    cnt = 0 
    isLie = False
    
    for party in parties:
        for index in range(1, party[0]+1):
            if party[index]-1 not in can:
                isLie = True
        if isLie == False : cnt += 1
        else : isLie = False

    return cnt

if __name__ == "__main__":
    # pp[0] : people
    # pp[1] : party
    pp = list(map(int, input().split()))
    start = list(map(int, input().split()))
    nodes = [list(map(int, input().split())) for _ in range(pp[1])]

    if start[0] == 0 :
        print(pp[1])
    else:
        mat = initailized_matrix(pp[0], nodes)
        people = {i for i in range(pp[0])}
        tmp = set()
        for i in range(1, start[0]+1):
            tmp = tmp | set(start_bfs(mat, start[i], pp[0]))
        
        can_lie = people - tmp
        print(get_num_party(nodes, can_lie))

# 13 12
# 3 1 5 7
# 2 1 2 
# 1 3
# 3 2 3 4
# 1 5
# 1 6
# 2 5 6
# 3 7 8 9
# 1 8
# 1 9
# 2 8 9
# 3 11 12 13
# 2 10 11