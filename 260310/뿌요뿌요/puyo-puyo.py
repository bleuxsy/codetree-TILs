def dfs(x, y ):
    block = 1
    num = grid[x][y]

    for dx, dy in [(1, 0), (-1, 0), (0 , 1), (0, -1)]:
        nx , ny = x + dx, y + dy

        if 0<= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if  grid[nx][ny] == num:
                visited[nx][ny] = True
                block += dfs(nx, ny)
    
    return block 


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
blocks = []
# Please write your code here.
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            blocks.append(dfs(i, j))



bomb = 0
max_bomb = 0
for b in blocks:
    if b >= 4:
        bomb += 1
    max_bomb = max(max_bomb, b)

print(bomb, max_bomb)