from collections import deque

q = deque()
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

INF = 10**9
dp = [[[INF, -INF] for _ in range(n)] for _ in range(n)]

dp[0][0] = [grid[0][0], grid[0][0]]
q.append((0, 0))

while q:
    cx, cy = q.popleft()

    for dx, dy in [(1, 0), (1, 1)]:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < n and 0 <= ny < n:
            new_min = min(dp[cx][cy][0], grid[nx][ny])
            new_max = max(dp[cx][cy][1], grid[nx][ny])

         
            if new_min != dp[nx][ny][0] or new_max != dp[nx][ny][1]:
                dp[nx][ny][0] = new_min
                dp[nx][ny][1] = new_max
                q.append((nx, ny))

print(dp[n-1][n-1][1] - dp[n-1][n-1][0])