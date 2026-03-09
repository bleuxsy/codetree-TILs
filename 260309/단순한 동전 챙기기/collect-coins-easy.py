def move(sx, sy, L, num):
    global answer, best

    if L >= answer:
        return

    last_num = -1 if not num else num[-1]
    state = (sx, sy, last_num, len(num))
    if state in best and best[state] <= L:
        return
    best[state] = L

    if grid[sx][sy] == 'E':
        if len(num) >= 3:
            answer = min(answer, L)
        return

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = sx + dx
        ny = sy + dy

        if 0 <= nx < n and 0 <= ny < n:
            cell = grid[nx][ny]

            # 숫자 칸인 경우
            if cell not in ['.', 'E', 'S']:
                val = int(cell)

                # 1) 안 먹고 그냥 지나가기
                move(nx, ny, L + 1, num)

                # 2) 먹고 지나가기
                if not num:
                    move(nx, ny, L + 1, [val])
                elif val > num[-1]:
                    move(nx, ny, L + 1, num + [val])

            else:
                move(nx, ny, L + 1, num)

 


INF = 10 ** 18
n = int(input())
grid = [list(input()) for _ in range(n)]
answer = INF
total = 0
best = {}

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            sx, sy = i, j
        elif grid[i][j] == '.' or grid[i][j] == 'E':
            continue
        else:
            total += 1

if total < 3:
    print(-1)
else:
    move(sx, sy, 0, [])
    print(-1 if answer == INF else answer)