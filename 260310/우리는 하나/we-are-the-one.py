from collections import deque
def bfs():
    global answer

    visited = [[False] * n for _ in range(n)]
    stack = deque()
    for x, y in picked:
        visited[x][y] = True
        stack.append((x, y))
    t= len(picked)
    while stack:
        sx, sy = stack.popleft()

        for dx, dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            nx , ny = sx + dx , sy + dy
            if 0<= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and u <= abs(grid[nx][ny] - grid[sx][sy]) <= d:
                    stack.append((nx,ny))
                    t += 1
                    visited[nx][ny] = True

    return t
def choose(start, depth):
    global answer

    if depth == k:
        answer = max(answer, bfs())
        return
    for idx in range(start, len(city)):
        picked.append(city[idx])
        choose(idx+1, depth+1)
        picked.pop()
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
picked = []
city = []
answer = 0

for i in range(n):
    for j in range(n):
        city.append((i, j))

choose(0, 0)

print(answer)