from collections import deque
N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input().strip()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

sd = 0
stack = deque()
stack.append((x, y, sd))
time = 1

visited = [[0] * (N + 1) for _ in range(N + 1)]
visited[x][y] = 1

while stack:
    sx, sy, sd = stack.popleft()

    nx = sx + dx[sd]
    ny = sy + dy[sd]

    if 1 <= nx <= N and 1 <= ny <= N:
        if visited[nx][ny] == 0:
            if grid[nx][ny] == ".":
                
                nd = (sd + 3) % 4

                rx = nx + dx[nd]
                ry = ny + dy[nd]

                
                if 1 <= rx <= N and 1 <= ry <= N and grid[rx][ry] == ".":
                    visited[nx][ny] = 1
                    visited[rx][ry] = 1
                    stack.append((rx, ry, nd))
                    time += 2
                else:
                    visited[nx][ny] = 1
                    stack.append((nx, ny, sd))
                    time += 1
            else:
                # 벽이면 방향만 바꿈
                nd = (sd + 1) % 4
                stack.append((sx, sy, nd))
        else:
            print(-1)
            break
    else:
        print(time)
        break