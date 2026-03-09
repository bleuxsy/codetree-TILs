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

          
            if cell not in ['.', 'E', 'S']:
                val = int(cell)

                
                move(nx, ny, L + 1, num)

               
                if not num:
                    move(nx, ny, L + 1, [val])
                elif val > num[-1]:
                    move(nx, ny, L + 1, num + [val])

            else:
                move(nx, ny, L + 1, num)