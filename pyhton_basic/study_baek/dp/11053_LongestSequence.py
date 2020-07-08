# 6
# 10 20 10 30 20 50

# 10
# 10

# 20
# 10 20

# 10
# 10 20

# 30
# 10 20 30

# 20 
# 10 20 30

# 50
# 10 20 30 50

def lis_algoritm_dp(arr, size):
    result = list()
    while arr:
        sequence = arr.pop(0)
        if result:
            isFlag = True
            for i in range(len(result)):
                if result[i] >= sequence:
                    result[i] = sequence
                    isFlag = False
                    break
            if isFlag:
                result.append(sequence)
        else:
            result.append(sequence)
            
    return result

if __name__ == "__main__":
    num = int(input())
    arr = list(map(int, input().split()))

    result = lis_algoritm_dp(arr, num)
    print(len(result))



# 4
# 1 4 2 3

# 6
# 1 2 1 1 1 1

# 12
# 1 2 3 4 5 4 3 2 1 2 3 4