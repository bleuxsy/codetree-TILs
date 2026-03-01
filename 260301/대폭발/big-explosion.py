from collections import deque
stack = deque()
n, m, r, c = map(int, input().split())
# Please write your code here.
answer = 0
grid = [[0]*n for _ in range(n)]
grid[r-1][c-1] = 1

# 폭탄이 있는 곳은 1 , 없는 곳은 0
def bumb(lst, t):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dt = 2**(t)
   
    while lst:
        
        sx, sy = lst.pop()
        
        for d in range(4):
            nx = int(sx + dx[d]*dt)
            ny = int(sy + dy[d]*dt)
            
            if 0<= nx< n and 0<= ny < n and grid[nx][ny]== 0:
                
                grid[nx][ny] = 1
    
    return 


for T in range(m):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                stack.append((i,j))
    bumb(stack, T)


# 결과 
for r in grid:
    answer += sum(r)
print(answer)