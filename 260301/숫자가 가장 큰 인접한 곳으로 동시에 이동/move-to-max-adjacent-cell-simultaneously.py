from collections import deque

n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 구슬 위치 표기

cnt = list([0]*n for _ in range(n))
for R,C in marbles:
    cnt[R-1][C-1] = 1

def move():

    for i in range(n):
        for j in range(n):
            if cnt[i][j] == 1:
                #구슬 위치 확인
                sx = i
                sy = j
                stack = []
                for d in range(4):
                    nx = sx+ dx[d]
                    ny = sy + dy[d]
                    if 0<= nx < n and 0 <= ny <n:
                        stack.append((d, a[nx][ny]))
                
                # 값 기준으로 정렬, 같은 경우는 d로 정렬
                stack.sort(key = lambda x : (-x[1], x[0]))
                ed , e = stack[0]
                cnt[sx][sy] = 0
                cnt[sx+dx[ed]][sy+dy[ed]] += 1
    

    return 
def cancel():
    for i in range(n):
        for j in range(n):
            if cnt[i][j] > 1:
                cnt[i][j] = 0

    return 



# t번 이동시키기
for _ in range(t):
    move()
    cancel()
# 구슬 개수 세기
answer =0
for b in cnt:
    answer += sum(b)
print(answer)
# Please write your code here.
