# 1 ~ N 개의 집
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.


# 3
# R  G  B
# 26 40 83
# 49 60 57
# 13 89 99

if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0,0,0] for _ in range(N)]

    dp[0][0] = matrix[0][0]
    dp[0][1] = matrix[0][1]
    dp[0][2] = matrix[0][2]

    for i in range(1,N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + matrix[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + matrix[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + matrix[i][2]

    print(dp[N-1][0:3])
    cost = min(dp[N-1][0:3])
    print(cost)