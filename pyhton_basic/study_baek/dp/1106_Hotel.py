# C(목표인원) N(도시개수)
# 비용  기댓값

import sys
import math
# n = 4
# cost = 3 , 5
# 1 2 3 / 5
# 4 5 6 / 10

def dp(c, n, rules):
    dp = [9999999999999 for _ in range(C+1)]
    dp[0] = 0
    for rule in rules:
        if dp[1] > rule[0]:
            dp[1] = rule[0]

    for i in range(2, c+1, 1):
        for rule in rules:
            if i - rule[1] < 0:
                dp[i] = min(dp[i], rule[0])
            else:
                value = min(dp[i-1] + rule[0], dp[i - rule[1]] + rule[0])
                dp[i] = min(dp[i], value)

    print(dp[c])

if __name__ == "__main__":
    C, N = map(int, sys.stdin.readline().split())
    rules = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
     
    if C > 0 and C <= 1000 and N <= 20:
        dp(C, N, rules)
    else: 
        print("0")
