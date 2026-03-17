n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

values = sorted(set(num for row in grid for num in row))

def can(low, high):
    if not (low <= grid[0][0] <= high):
        return False
    if not (low <= grid[n-1][n-1] <= high):
        return False

    dp = [[False] * n for _ in range(n)]
    dp[0][0] = True

    for i in range(n):
        for j in range(n):
            if not (low <= grid[i][j] <= high):
                continue

            if i == 0 and j == 0:
                continue

            if i > 0 and dp[i-1][j]:
                dp[i][j] = True
            if j > 0 and dp[i][j-1]:
                dp[i][j] = True

    return dp[n-1][n-1]

answer = 10**9

for i in range(len(values)):
    for j in range(i, len(values)):
        low = values[i]
        high = values[j]

        if can(low, high):
            answer = min(answer, high - low)

print(answer)