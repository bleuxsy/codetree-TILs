from collections import deque


def bfs(x, y, cnt):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    stack = []

    if cnt == k:
        print(x+1 , y +1)
        return
    while q:

        sx, sy = q.popleft()
        visited[sx][sy] = True
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = sx + dx
            ny = sy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] < grid[x][y]:
                    q.append((nx, ny))
                    stack.append((grid[nx][ny], nx, ny))
                    visited[nx][ny] = True
    if stack:
        stack.sort(key = lambda x: (-x[0], x[1], x[2]))
        
        _ , nxt , nxy = stack[0]

        bfs(nxt, nxy, cnt+1)
    else:
        print(x + 1, y + 1)
        return



n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())

# Please write your code here.

bfs(r - 1, c - 1, 0)