from collections import deque

def melt():
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    ice = []

    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True

                if a[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    ice.append((nx, ny))

    for x, y in ice:
        a[x][y] = 0

    return len(ice)


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

time = 0
last = 0

while True:
    melted = melt()

    if melted == 0:
        break

    time += 1
    last = melted

print(time, last)