import copy

n, m, Q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(Q)]

# Please write your code here.
def move(x1, y1, x2, y2):
    temp = a[x1][y1]  

    
    for x in range(x1, x2):
        a[x][y1] = a[x+1][y1]

    for y in range(y1, y2):
        a[x2][y] = a[x2][y+1]

    for x in range(x2, x1, -1):
        a[x][y2] = a[x-1][y2]
    
    for y in range(y2, y1+1, -1):
        a[x1][y] = a[x1][y-1]

    a[x1][y1+1] = temp  

    
   
    
def check(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0 , -1]
    total = a[x][y]
    num = 1
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<= nx< n and 0<= ny <m :
            total += a[nx][ny]
            num += 1
    

    return total//num

for q in range(Q):

    r1, c1, r2, c2 = winds[q]
    move(r1-1, c1-1, r2-1, c2-1)
    b = copy.deepcopy(a)
    
    for i in range(r1-1, r2):
        for j in range(c1-1, c2):
            b[i][j] = check(i, j)

    a= b
for r in b:
    print(*r)