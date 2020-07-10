# 문제
# 첫째 줄에 발전소의 개수 N이 주어진다. N은 16보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에는 발전소 i를 이용해서 발전소 j를 재시작할 때 드는 비용이 주어진다. 
# 그 다음 줄에는 각 발전소가 켜져있으면 Y, 꺼져있으면 N이 순서대로 주어진다.
# 마지막 줄에는 P가 주어진다. 비용은 50보다 작거나 같은 음이 아닌 정수이고, P는 0보다 크거나 같고, N보다 작거나 같은 정수이다.

#첫째 줄에 비용의 최솟값을 출력한다. 불가능한 경우에는 -1을 출력한다.

# matrix[i][j] = i번째 발전소가 j번째 발전소를 운영할 때 드는 비용
# Y = 작동, N = 고장
# P = 발전소 작동 갯수(0<=P<=N) 

# 3
# 0 10 11
# 10 0 12
# 12 13 0
# YNN
# 3

# 21

# 3
# 0 20 21
# 10 0 10
# 13 21 0
# NNY
# 30

def visit(mat, size, isOperated):
    start = int()
    for i in range(len(isOperated)):
        if isOperated[i] == 'Y':
            start = i
            for j in range(size):
                mat[j][i] = 0
    return mat, start


def dijkstra(mat, size, start): 
    cost = [i for i in mat[start]]
    nodes = {i for i in range(size)}
    visited = {start}

    for i in nodes - visited:
        for j in nodes:
            if i != j and cost[j-1] + mat[i][j] < cost[j]:
                cost[j] = cost[j-1] + mat[i][j]
        visited.add(i)

    return cost

if __name__ == "__main__":
    size = int(input())
    mat = [list(map(int, input().split())) for _ in range(size)]
    isOperated = list(input())
    fac_num = int(input())

    if 'Y' not in isOperated:
        if fac_num != 0 : print(-1)
        else: print(0)
    else:
        mat, start = visit(mat, size, isOperated)
        result = dijkstra(mat, size, start)
        result.sort()
        print(result)
        print(sum(result[:fac_num]))

# 5
# 0 10 11 30 11
# 10 0 12 8 7
# 12 13 0 48 23 
# 11 2 18 0 22 
# 21 8 30 7 0
# NYYYN
# 3 

# 배열 , 메모리 구조 , 포인터