# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
class Solution(object):
    def __init__(self, N, arr):
        self.n = N
        self.arr = arr
        # 행 j , 열 i
        # index : 0 / 4 5 2 6 5 
        # index : 1 / 2 7 4 4
        # index : 2 / 8 1 0
        # index : 3 / 3 8
        # index : 4 / 7

    def cost_explore(self):
        cost_list = list(self.arr[0])
        # cost_list = [4, 5, 2, 6, 5]
        
        for col in range(1, self.n):
            # col :: 1, 2, 3, 4
            # 2 7 4 4
            # 8 1 0
            # 3 8
            # 7
            tmp = list()
            for row in range(0, self.n - col):
                maximum = max(cost_list[row], cost_list[row+1])
                tmp.append(self.arr[col][row] + maximum)
            
            cost_list = tmp

        return cost_list[0]

if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.reverse()

    solution = Solution(N, arr)
    print(solution.cost_explore())