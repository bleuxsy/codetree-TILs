n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
row = []
res = 0
for i in range(n):
    flag = 1
    for j in range(1, n):
        if grid[i][j-1] == grid[i][j]:
            flag += 1
        else:
            flag = 1
    row.append(flag)

for r in row:
    if r >= m:
        res += 1
col = []
for i in range( n):
    for j in range(1,n):
        if grid[j-1][i] == grid[j][i]:
            flag += 1
        else:
            flag = 1
    col.append(flag)

for c in col:
    if c >= m:
        res += 1
print(res)
# Please write your code here.
