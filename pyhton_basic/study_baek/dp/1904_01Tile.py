# 1 과 00 조합으로 이진수를 만들 수 있는 경우의 수 % 15746

# input
# 4
#ouput
# 5

# 0000
# 0011
# 1001
# 1100
# 1111

# input  output
# 0 0
# 1 1
# 2 2
# 3 3
# 4 5
# 5 8
# 6 13
# 7 21
# 8 34
# 9 55
# => 피보나치

 

def make_fibonacci(size):
    mod = 15746
    fibo_arr = [0, 1, 2]

    for i in range(3, size+1):
        fibo_arr.append((fibo_arr[i-2] + fibo_arr[i-1]) % mod)

    return fibo_arr

if __name__ == "__main__":
    size = int(input())

    arr = make_fibonacci(size) 
    print(arr[size])
    
