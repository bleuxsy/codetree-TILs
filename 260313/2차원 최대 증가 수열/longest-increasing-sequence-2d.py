def solve(x, y):
    for i in range(x + 1, n):
        for j in range(y + 1, m):
            if grid[x][y] < grid[i][j]:
                dp[i][j] = max(dp[x][y] + 1, dp[i][j])
                solve(i, j)

    return


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * m for _ in range(n)]

# Please write your code here.
answer = 0
solve(0, 0)
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[i][j])
print(answer)