from collections import deque
N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# Please write your code here.

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
sd = 0
stack = deque()
stack.append((x,y, sd))
time = 1
visited = list([0]*(N+1) for _ in range(N+1))
visited[x][y] = 1
while stack:
    sx , sy , sd = stack.popleft()
    
    #진행 방향의 다음 칸
    nx = sx + dx[sd]
    ny = sy + dy[sd]
    if 1<= nx <= N and 1<= ny <= N :
    #다음 칸에 벽이 없을 때,
        if visited[nx][ny] == 0:
            if grid[nx][ny] == ".":
                #오른쪽에 벽이 없을 때,
                nd = sd - 1
                if grid[nx+dx[nd]][ny+dy[nd]] == ".":
                    visited[nx][ny] = 1
                    visited[nx+dx[nd]][ny+dy[nd]] = 1
                    stack.append((nx+dx[nd],ny+dy[nd], nd))
                    time += 2
                else:
                    visited[nx][ny] = 1
                    stack.append((nx, ny, sd))
                    time += 1
            #진행방향에 벽이 있을 때
            else:
                nd = sd +1
                stack.append((sx, sy, nd))
        else:
            print(-1)
            break
    # 미로 끝
    else:
        print(time)
        break

