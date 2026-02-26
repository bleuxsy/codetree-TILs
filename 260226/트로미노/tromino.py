n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 4방향 중에 값이 제일 큰 것 위주로 선택 3번 하기
answer = 0
def first(x, y, L, t):
    global answer
    bigger = 0
    mx = 0
    my = 0
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0 ]
    if L == 2:
        answer = max(answer, t)
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
                
                visited[nx][ny] = 1
                first(mx, my, L+1, t + bigger)
    return 
    
max_row = 0
max_col = 0
max_val = grid[0][0]


# Please write your code here.
for i in range(n):
    for j in range(m):
        if grid[i][j] >= max_val:
            max_val = grid[i][j]
            max_row = i
            max_col = j
            
            visited = list([0] * m for _ in range(n))
            visited[max_row][max_col] = 1
            #answer = first(max_row, max_col, 0, max_val)
            first(max_row, max_col, 0, max_val)
            
print(answer)
        