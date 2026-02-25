n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def ok_line(lst, m):
    run = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            run += 1
            if run >= m:
                return 1
        else:
            run = 1
    return 1 if m == 1 else 0

res = 0

# rows
for r in grid:
    res += ok_line(r, m)

# cols
for c in range(n):
    col = [grid[r][c] for r in range(n)]
    res += ok_line(col, m)

print(res)