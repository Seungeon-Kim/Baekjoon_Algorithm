# 상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다.
# ㅁ  ㅁ - ㅁ
# 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.

# 상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.

# 6
# 5
# 1 2
# 1 3
# 3 4
# 2 3
# 4 5

# 3
def bfs(queues, queue):
    result = list()
    while(queue):
        q = queue.pop(0)
        if queues[q]:
            for val in queues[q]:
                result.append(val)
    return result

if __name__ == "__main__":
    num = int(input())
    size = int(input())
    arr = [list(map(int, input().split())) for _ in range(size)]

    queues = [list() for _ in range(num)]
    for element in arr:
        queues[element[0]-1].append(element[1]-1)

    result = set()

    for my in queues[0]:
        result.add(my)


    tmp = [val for val in range(result)]
    for fr in tmp:
        for val in queues[fr]:
            result.add(val)

    print(result)