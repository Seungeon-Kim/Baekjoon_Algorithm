
# 2 4
# CAAB
# ADCB

# 3 4
# ABCD
# BCDE
# FECD
class Solution(object):
    max = 0
    stack = []
    movable = [(0,1),(0,-1),(1,0),(-1,0)]
    def __init__(self, row, col, mat):
        self.row = row
        self.col = col
        self.mat = mat
        self.start_dfs()
        
    def start_dfs(self):
        Solution.stack.append(self.mat[0][0])
        self.depth_first_search(0, 0, 1)
        print(Solution.max)

    def depth_first_search(self, cr, cc, cnt): 
        # print("cr, cc :: ", cr, " ", cc )
        for mv in self.movable :
            nr = cr + mv[0]
            nc = cc + mv[1]
            if self.row > nr >= 0 and self.col > nc >= 0:
                if self.mat[nr][nc] not in Solution.stack:
                    Solution.stack.append(self.mat[nr][nc])
                    Solution.max = max(Solution.max, cnt+1)
                    self.depth_first_search(nr, nc, cnt+1)
        Solution.stack.pop()

if __name__ == "__main__":
    row, col = map(int, input().split())
    arr = [list(input()) for _ in range(row)]
    solution = Solution(row, col, arr)

