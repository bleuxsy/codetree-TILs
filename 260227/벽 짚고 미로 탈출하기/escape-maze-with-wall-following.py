N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input().strip()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# 0:E, 1:N, 2:W, 3:S (너 코드 그대로)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

sd = 0  # 시작 방향
time = 0

# 방문 체크는 (x,y,dir)
visited = [[[0]*4 for _ in range(N+1)] for __ in range(N+1)]
visited[x][y][sd] = 1

while True:
    right = (sd + 3) % 4   # 너 코드에서 sd-1이 의미하던 "오른쪽"을 안전하게

    # 1) 오른쪽 칸이 비어있으면: 오른쪽으로 회전 후 전진
    rx, ry = x + dx[right], y + dy[right]
    if 1 <= rx <= N and 1 <= ry <= N and grid[rx][ry] == ".":
        sd = right
        nx, ny = x + dx[sd], y + dy[sd]
    else:
        # 2) 아니면 앞 칸이 비어있으면: 그대로 전진
        nx, ny = x + dx[sd], y + dy[sd]
        # 앞이 벽이면: 왼쪽으로 회전(전진은 안 함)
        if 1 <= nx <= N and 1 <= ny <= N and grid[nx][ny] == "#":
            sd = (sd + 1) % 4
            # 방향만 바꿨으니 루프 체크
            if visited[x][y][sd]:
                print(-1)
                break
            visited[x][y][sd] = 1
            continue

    # 3) 전진했는데 격자 밖이면 탈출
    if not (1 <= nx <= N and 1 <= ny <= N):
        time += 1
        print(time)
        break

    # 4) 다음 칸이 벽이면(안전) 회전 처리
    if grid[nx][ny] == "#":
        sd = (sd + 1) % 4
        if visited[x][y][sd]:
            print(-1)
            break
        visited[x][y][sd] = 1
        continue

    # 5) 이동 + 상태 루프 감지
    time += 1
    x, y = nx, ny
    if visited[x][y][sd]:
        print(-1)
        break
    visited[x][y][sd] = 1