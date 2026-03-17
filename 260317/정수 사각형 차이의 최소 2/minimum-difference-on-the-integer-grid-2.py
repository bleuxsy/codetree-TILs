def dfs(x, y, nmin, nmax):
    global answer

    if x == n - 1 and y == n - 1:
        answer = min(answer, nmax - nmin)
        return

    for dx, dy in [(1, 0), (0, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                new_min = min(nmin, grid[nx][ny])
                new_max = max(nmax, grid[nx][ny])

                visited[nx][ny] = 1
                dfs(nx, ny, new_min, new_max)
                visited[nx][ny] = 0


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

INF = 10 ** 9
answer = INF

visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

dfs(0, 0, grid[0][0], grid[0][0])

print(answer)