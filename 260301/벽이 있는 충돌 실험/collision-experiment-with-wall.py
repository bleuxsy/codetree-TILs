T = int(input())

def move():
    global grid, N

    next_grid = [['*'] * N for _ in range(N)]
    cnt = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            d = grid[i][j]
            if d == '*':
                continue

            
            if d == 'L':
                nx, ny = i, j - 1
                if ny < 0:
                    nx, ny = i, j
                    d = 'R'

            elif d == 'R':
                nx, ny = i, j + 1
                if ny >= N:
                    nx, ny = i, j
                    d = 'L'

            elif d == 'U':
                nx, ny = i - 1, j
                if nx < 0:
                    nx, ny = i, j
                    d = 'D'

            else:  # 'D'
                nx, ny = i + 1, j
                if nx >= N:
                    nx, ny = i, j
                    d = 'U'

            
            cnt[nx][ny] += 1
            if cnt[nx][ny] == 1:
                next_grid[nx][ny] = d      # 첫 도착
            else:
                next_grid[nx][ny] = '*'    # 2개 이상이면 충돌로 비움

    grid = next_grid


for _ in range(T):
    N, M = map(int, input().split())
    grid = [['*'] * N for _ in range(N)]

    for _ in range(M):
        xi, yi, di = input().split()
        grid[int(xi) - 1][int(yi) - 1] = di

    for _ in range(100):
        move()

    answer = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] != '*':
                answer += 1
    print(answer)