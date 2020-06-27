# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    result = 0 

    arr.sort(reverse=True)

    for coin in arr:
        tmp = k % coin
        if tmp != k :
            result += int(k / coin)
            k = tmp
        if k == 0 : break

    print(result)