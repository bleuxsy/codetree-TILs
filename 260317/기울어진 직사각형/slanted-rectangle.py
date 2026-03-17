def find(x, y, a, b):
    p1 = (x, y)
    p2 = (x + a, y + a)
    p3 = (x + a + b, y + a - b)
    p4 = (x + b, y - b)

    # 범위 체크
    for px, py in [p1, p2, p3, p4]:
        if not (0 <= px < n and 0 <= py < n):
            return None

    return [p1, p2, p3, p4]


def addnum(points):
    p1, p2, p3, p4 = points
    total = 0

    x, y = p1
   

  
    while (x, y) != p2:
        x += 1
        y += 1
        total += grid[x][y]

   
    while (x, y) != p3:
        x += 1
        y -= 1
        total += grid[x][y]

  
    while (x, y) != p4:
        x -= 1
        y -= 1
        total += grid[x][y]

    
    while (x, y) != p1:
        x -= 1
        y += 1
        total += grid[x][y]

    return total


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for x in range(n):
    for y in range(n):
        for a in range(1, n):
            for b in range(1, n):
                points = find(x, y, a, b)
                if points is not None:
                    answer = max(answer, addnum(points))

print(answer)