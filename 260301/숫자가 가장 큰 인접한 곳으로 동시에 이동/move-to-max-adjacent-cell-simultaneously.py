from collections import deque

n, m, t = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
marbles = [tuple(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = [[0]*n for _ in range(n)]
for R, C in marbles:
    cnt[R-1][C-1] = 1

def move():
    global cnt
    next_cnt = [[0]*n for _ in range(n)]

    for sx in range(n):
        for sy in range(n):
            if cnt[sx][sy] == 1:
                stack = []
                for d in range(4):
                    nx = sx + dx[d]
                    ny = sy + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        stack.append((d, a[nx][ny]))

                # n==1 같은 경우 stack이 비는 상황 방어 (움직일 곳 없으면 그대로)
                if not stack:
                    next_cnt[sx][sy] += 1
                    continue

                # 값 내림차순, 같으면 d 오름차순
                stack.sort(key=lambda x: (-x[1], x[0]))
                ed, _ = stack[0]

                nx = sx + dx[ed]
                ny = sy + dy[ed]
                next_cnt[nx][ny] += 1

    cnt = next_cnt

def cancel():
    for i in range(n):
        for j in range(n):
            if cnt[i][j] > 1:
                cnt[i][j] = 0

for _ in range(t):
    move()
    cancel()

answer = sum(map(sum, cnt))
print(answer)