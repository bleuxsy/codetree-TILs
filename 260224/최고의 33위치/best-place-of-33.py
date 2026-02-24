n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
res = 0
def solved(x, y):
    total = 0
    for i in range(0,3):
        for j in range(0, 3):
            nx = x+i
            ny = y+j
            if 0<= nx < n and 0<= ny < n :
                total += grid[nx][ny]
            else:
                return 0
        
    return total 
# Please write your code here.
x, y = 0 , 0
for x in range(n):
    for y in range(n):
        res= max(solved(x, y), res)
print(res)