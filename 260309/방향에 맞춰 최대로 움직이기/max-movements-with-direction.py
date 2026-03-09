from collections import deque
n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

dir = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def find_pos(sx, sy, d, t):
    global answer
  
    dx , dy = dir[d]
    answer = max(answer, t)
    
    for i in range(1, n):
        nx , ny = sx + dx * i , sy + dy * i 
        if 0<= nx < n and 0<= ny < n:
            if num[nx][ny] > num[sx][sy]:
                find_pos(nx, ny, move_dir[nx][ny], t+1)
            
        else:
            break
    
    return 
    



answer = 0
find_pos(r-1, c-1, move_dir[r-1][c-1], 0)
# Please write your code here.
print(answer)