def initialize():
    for i in range(n):
        for j in range(n):
            dp[i][j] = INF

    # 1열 막행 초기화
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], grid[i][0])

    for j in range(1, n):
        dp[0][j] = max(dp[0][j - 1], grid[0][j])


def solve(lower):
    for i in range(n):
        for j in range(n):
            if grid[i][j] < lower:
                grid[i][j] = INF
    initialize()

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

    return dp[n - 1][n - 1]


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
INF = 10 * 8
ans = INF
dp = [[0] * n for _ in range(n)]
for lower in range(1, 101):
    upper = solve(lower)

    if upper == INF:
        continue
    ans = min(ans, upper - lower)

print(ans)