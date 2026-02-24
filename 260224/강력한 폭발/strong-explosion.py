n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bombs = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))

max_area = 0


def explode(x, y, bomb_type):
    changed = []

    if bomb_type == 0:  # first (세로 5칸)
        for i in range(x - 2, x + 3):
            if 0 <= i < n and grid[i][y] == 0:
                grid[i][y] = 1
                changed.append((i, y))

    elif bomb_type == 1:  # second (상하좌우)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                changed.append((nx, ny))

    else:  # third (대각선)
        dx = [1, 1, -1, -1]
        dy = [1, -1, -1, 1]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                changed.append((nx, ny))

    return changed


def restore(changed):
    for x, y in changed:
        grid[x][y] = 0


def dfs(idx):
    global max_area

    if idx == len(bombs):
        count = sum(sum(row) for row in grid)
        max_area = max(max_area, count)
        return

    x, y = bombs[idx]

    for bomb_type in range(3):
        changed = explode(x, y, bomb_type)
        dfs(idx + 1)
        restore(changed)


dfs(0)
print(max_area)