import sys

result = set()

def convert(matrix):
    dic = dict()
    for start in matrix:
        if start[0] not in dic.keys():
            dic[start[0]] = list()
        dic[start[0]].append(start[1])
    return dic

def bfs(k, visited, dic, starts):
    if k > 0:
        nextNodes = list()
        for start in starts:
            if start in dic.keys():
                nodes = [nextNode for nextNode in dic[start] if nextNode not in visited]
                nextNodes.extend(nodes)
                visited.update(nextNodes)                
        bfs(k-1, visited, dic, nextNodes)
    elif k == 0:
        result.update(starts)               

if  __name__ == "__main__":
    N, M, K, X = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _  in range(M)]

    dic = convert(matrix)
    visited = {X}
    bfs(K, visited, dic, [X])    

    if len(result) == 0:
        print("-1")
    else:
        resultToArray = sorted(result)
        for value in resultToArray:
            print(value)






# def dfs(dic, start, k, visited):
#     if k > 0 and start in dic.keys():
#         for element in dic[start]:
#             if element not in visited:
#                 if element in result:
#                     removed.add(element)

#                 visited.add(element)
#                 dfs(dic, element, k-1, visited)
#     elif k == 0 and start in dic.keys():
#         for element in dic[start]:
#             if element not in visited:
#                 result.append(element)

# def print_result():
#     new_list = [new_result for new_result in result if new_result not in removed]
#     if len(new_list) == 0:
#         print("-1")
#     else:
#         new_list.sort()
#         for value in new_list:
#             print(value)

    # visited = {X}
    # dfs(dic, X, K-1, visited)
    # print_result()