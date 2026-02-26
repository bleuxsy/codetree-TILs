n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 4방향 중에 값이 제일 큰 것 위주로 선택 3번 하기
answer = 0
def first(x, y, L, t):
    global answer
    bigger = -1
    mx = x
    my = y
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0 ]
    if L == 2:
        answer = max(answer, t)
        #print(f"t", t)
        return 
    for d in range(4):
        nx = dx[d] + x
        ny = dy[d] + y
        #값이 제일 큰 것 찾기 .. 
        if 0<= nx < n and 0<= ny <m and visited[nx][ny] == 0:
            if bigger <= grid[nx][ny] :
                bigger = grid[nx][ny]
                mx = nx
                my = ny
                #print(f"mx, my, bigger", mx, my, bigger)
                visited[nx][ny] = 1
                first(mx, my, L+1, t + bigger)
                visited[nx][ny] = 0
    return 
    
max_row = 0
max_col = 0
max_val = grid[0][0]

max_val = max(max(row) for row in grid)
xy = []
# Please write your code here.
for i in range(n):
    for j in range(m):
        if grid[i][j] == max_val:
            #print(f"max_row, max_col", i, j)
            visited = list([0] * m for _ in range(n))
            visited[i][j] = 1
            #answer = first(max_row, max_col, 0, max_val)
            first(i, j, 0, max_val)
            
print(answer)
        