INF = 10**18
n = int(input())
grid = [list(input()) for _ in range(n)]

sx = sy = -1
total = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            sx, sy = i, j
        elif grid[i][j] not in ['S', 'E', '.']:
            total += 1

if total < 3:
    print(-1)
    exit()

answer = INF
best = {}

def backtrack(x, y, last_num, cnt, dist):
    global answer

    # 이미 정답보다 길면 중단
    if dist >= answer:
        return

   
    state = (x, y, last_num, cnt)
    if state in best and best[state] <= dist:
        return
    best[state] = dist

    
    if grid[x][y] == 'E':
        if cnt >= 3:
            answer = min(answer, dist)
        return

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < n and 0 <= ny < n):
            continue

        cell = grid[nx][ny]

        
        if cell not in ['S', 'E', '.']:
            num = int(cell)
            if num > last_num:
                backtrack(nx, ny, num, cnt + 1, dist + 1)

        
        else:
            backtrack(nx, ny, last_num, cnt, dist + 1)

backtrack(sx, sy, -1, 0, 0)

print(-1 if answer == INF else answer)