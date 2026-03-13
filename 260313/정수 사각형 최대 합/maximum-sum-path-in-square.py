n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]* n for _ in range(n)]
# Please write your code here.
def initialize():
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0]  = dp[i-1][0]+ grid[i][0]

    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]

initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

for g in dp:
    print(*g)
print(max(dp[n-1]))
