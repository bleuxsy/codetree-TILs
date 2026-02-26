n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
answer = -10**18

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt, total):
    global answer
    # cnt = 지금까지 선택한 칸 개수
    if cnt == 3:  # 총 4칸(=이동 3번)
        answer = max(answer, total)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, total + grid[nx][ny])
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, grid[i][j])
        visited[i][j] = 0

print(answer)