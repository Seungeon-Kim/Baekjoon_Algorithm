result = 0 

def bfs(numbers, i, length, target, value):
    global result
    if  i == length and value == target:
        result = result + 1
    elif i < length:
        bfs(numbers, i+1, length, target, value - numbers[i])
        bfs(numbers, i+1, length, target, value + numbers[i])


def solution(numbers, target):
    global result
    length = len(numbers)
    bfs(numbers, 0, length, target, 0)
    return result

if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    expected = 5  

    print(solution(numbers, target))