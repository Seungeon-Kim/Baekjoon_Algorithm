# size
# 10

# arr
# 10 -4 3 1 5 6 -35 12 21 -1

# tmp
# 10 6 9 10 15 21 -14 -2 33 23

if __name__ == "__main__":
    size = int(input())
    arr = list(map(int, input().split()))

    # tmp = [arr[0] if arr[0] >= 0 else 0]
    tmp = [arr[0]]
    for index in range(1, size):
        maximum = max(arr[index-1], tmp[index-1])

        if maximum + arr[index] < arr[index]:
            tmp.append(arr[index])
        else: tmp.append(maximum + arr[index])
    
    tmp.sort()
    print(tmp[size-1])


