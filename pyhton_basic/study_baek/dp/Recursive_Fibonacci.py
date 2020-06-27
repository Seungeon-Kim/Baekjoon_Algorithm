class Fibonacci(object):
    zero_num = 0 
    one_num = 0

    def __init__(self, n):
        self.cv_init()
        self.recursive_fib(n)

    def cv_init(self):
        Fibonacci.zero_num = 0
        Fibonacci.one_num = 0
    
    def recursive_fib(self, n : int):
        if n == 0 :
            Fibonacci.zero_num += 1
            return 0
        elif n == 1 :
            Fibonacci.one_num += 1
            return 1
        else :
            return self.recursive_fib(n-1) + self.recursive_fib(n-2)

    def get_result(self):
        return Fibonacci.zero_num, Fibonacci.one_num

if __name__ == "__main__":
    N = int(input())
    arr = list()
    for i in range(0, N):
        arr.append(int(input()))

    print(arr)
    
    for i in range(0, N):
        module = Fibonacci(arr[i])
        zero, one = module.get_result()
        print(zero, ' ', one)
    