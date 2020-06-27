class Fibonacci(object):
    zero_fib =list([1,0])
    one_fib = list([0,1])

    def __init__(self):
        self.pre_fib()

    def pre_fib(self):
        for i in range(2, 41):
            Fibonacci.zero_fib.append(Fibonacci.zero_fib[i-2] + Fibonacci.zero_fib[i-1])
            Fibonacci.one_fib.append(Fibonacci.one_fib[i-2] + Fibonacci.one_fib[i-1])
 
    def get_elemets(self, index):
        return Fibonacci.zero_fib[index], Fibonacci.one_fib[index]


if __name__ == "__main__":
    module = Fibonacci()
    indexies = list()

    N = int(input())

    for i in range(0, N):
        indexies.append(int(input()))
    
    for index in indexies:
        zero, one = module.get_elemets(index)
        print(str(zero)+ " "+ str(one))