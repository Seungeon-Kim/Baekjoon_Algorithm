# 4
# 2 1 1 0

# 4 2 1 3

# 4
# 3 2 1 0
# 4 3 2 1     
if __name__ == "__main__":
    n = int(input())
    index = list(map(int, input().split()))
    index.reverse()
    result = list()

    for ind in index:
        if ind == 0 :
            result.insert(ind, n)
        else :
            cnt = 0
            i = 0

            for element in result:
                if element > n : cnt += 1
                if cnt == ind :
                    break
                i += 1
            result.insert(i+1, n)
        n = n - 1 


    prt = ''
    for i in result:
       prt += str(i) + " "
    print(prt[:-1])
