# 3 4
# 1 2 3 4
# 0 0 0 5
# 9 8 7 6
class Solution(object):
    def __init__(self, col, row, arr):
        self.col = col
        self.row = row
        self.arr = arr
        self.initailized_matrix()

    def initailized_matrix(self):
        self.tmp = [0] * self.col
        for i in range (0, self.col):
            self.tmp[i] = [0] * self.row

        self.tmp[0][0] = self.arr[0][0]
        for r in range(1, self.row):
            self.tmp[0][r] = self.arr[0][r] + self.tmp[0][r-1]

        for c in range(1, self.col):
            self.tmp[c][0] = self.arr[c][0] + self.tmp[c-1][0]


    def recurrence_matrix(self):
        for c in range(1, self.col):
            for r in range(1, self.row):
                self.tmp[c][r] = self.arr[c][r] + max(self.tmp[c-1][r-1], self.tmp[c][r-1], self.tmp[c-1][r])
        
        
        return self.tmp[self.col-1][self.row-1]
        

if __name__ == "__main__":
    # col, row = 3, 4
    # arr = [[1,2,3,4],[0,0,0,5],[9,8,7,6]]

    NM = input().split()
    col = int(NM[0])
    row = int(NM[1])
    arr = [list(map(int, input().split())) for _ in range(col)]

    solution = Solution(col, row, arr)
    print(solution.recurrence_matrix())