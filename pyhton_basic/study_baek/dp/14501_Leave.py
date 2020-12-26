import sys
 
def solve(n, t, p):
    dp = [0 for _ in range(n)]

    if t[n-1] == 1:
        dp[n-1] = p[n-1]

    for i in range(n-2, -1, -1): 
        end = i + t[i]

        if end == n:
            dp[i] = max(p[i], dp[i+1])
        elif end < n:
            dp[i] = max(p[i] + dp[end], dp[i+1])
        else:
            dp[i] = dp[i+1]
    print(dp[0])
 
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    t = []
    p = []
 
    for i in range(n):
        ti, pi = map(int, sys.stdin.readline().split())
        t.append(ti)
        p.append(pi)
    solve(n, t, p)