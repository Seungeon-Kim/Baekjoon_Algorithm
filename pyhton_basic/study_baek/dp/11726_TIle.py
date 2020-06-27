# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
class Solution(object):
    def __init__(self):
        length = 1001
        self.fib = [0] * length
        self.fib[1], self.fib[2] = 1, 2

        for i in range(3, length):
            self.fib[i] = self.fib[i-1] + self.fib[i-2]
    
    def get_result(self, n):
        return self.fib[n] % 10007


if __name__ == "__main__":
    i = int(input())
    solution = Solution()

    print(solution.get_result(i))