from collections import deque
def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x,y, 0))
    visited[x][y] = True


    while q:
        cx, cy, dist = q.popleft()
        if grid[cx][cy] == 3:
            return dist

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist+1))

    return -1


n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]
# Please write your code here.
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            answer[i][j] = bfs(i, j)

for r in answer:
    print(*r)