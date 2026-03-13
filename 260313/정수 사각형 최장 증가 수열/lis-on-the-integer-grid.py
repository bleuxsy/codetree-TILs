n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[1] * n for _ in range(n)]

cells = []
for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))

cells.sort()  # 작은 값부터

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for value, x, y in cells:
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] > grid[x][y]:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dp[i][j])

print(answer)