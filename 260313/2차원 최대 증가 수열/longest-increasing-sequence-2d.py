def solve(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(x + 1, n):
        for j in range(y + 1, m):
            if grid[x][y] < grid[i][j]:
                dp[x][y] = max(dp[x][y], solve(i, j) + 1)

    return dp[x][y]


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

# Please write your code here.
answer = 0
solve(0, 0)
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[i][j])
print(answer)