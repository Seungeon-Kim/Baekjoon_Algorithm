# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 10
# 20
# 14
# 18
# 17

#     0 1 2 3 4

# 0   0 1 1 1 0 
# 1   0 0 0 0 0
# 2   0 0 0 1 1          
# 3   0 0 0 0 0 
# 4   0 0 0 0 0


def initailized_matrix(arr, size):
    matrix = [[0 for i in range(size)] for _ in range(size)]

    for i in range(size):
        for j in arr[i][1:-1]:
            matrix[j-1][i] = 1

    return matrix

def topological_sort(starts, mat, size):
    queue = starts
    cycle = list()

    while queue:
        node = queue.pop(0)
        cycle.append(node)

        links = mat[node]
        for index in range(size):
            if links[index] == 1:
                if index in queue: queue.remove(index)
                if index in cycle : cycle.remove(index)
                queue.append(index)

    return cycle

def result(arr, cycle, cost, size):
    for now in cycle:
        max_cost = 0
        for build in arr[now][1:-1]:
            max_cost = max(max_cost, cost[build-1])

        cost[now] += max_cost


if __name__ == "__main__":
    size = int(input())
    arr = list() 
    cost = list()
    starts = list()

    for i in range(size):
        tmp =list(map(int, input().split()))
        if len(tmp) == 2: starts.append(i)
        arr.append(tmp)
        cost.append(tmp[0])

    matrix = initailized_matrix(arr,size)

    cycle = topological_sort(starts, matrix, size)
    result(arr, cycle, cost, size)

    for result in cost:
        print(result)