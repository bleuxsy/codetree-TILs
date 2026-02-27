# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]
from collections import deque

# Read direction
dir = input()

def left(lst):
    newgrid = [[0]*4 for _ in range(4)]
    for i in range(4):
        # 1) 왼 -> 오로 0 아닌 값 모으기
        vals = []
        for j in range(4):
            if lst[i][j] != 0:
                vals.append(lst[i][j])

        # 2) 왼쪽부터 합치기
        temp = deque()
        k = 0
        while k < len(vals):
            if k + 1 < len(vals) and vals[k] == vals[k+1]:
                temp.append(vals[k] * 2)
                k += 2
            else:
                temp.append(vals[k])
                k += 1

        # 3) 오른쪽에 0 채워서 길이 4 맞추기
        while len(temp) < 4:
            temp.append(0)

        # 4) 행에 왼쪽부터 채우기
        for j in range(4):
            newgrid[i][j] = temp[j]

    for r in newgrid:
        print(*r)

def right(lst):
    newgrid = [[0]*4 for _ in range(4)]
    for i in range(4):
        # 1) 오 -> 왼으로 0 아닌 값 모으기 (right-first)
        vals = []
        for j in range(3, -1, -1):
            if lst[i][j] != 0:
                vals.append(lst[i][j])

        # 2) 오른쪽부터 합치기
        temp = deque()
        k = 0
        while k < len(vals):
            if k + 1 < len(vals) and vals[k] == vals[k+1]:
                temp.append(vals[k] * 2)
                k += 2
            else:
                temp.append(vals[k])
                k += 1

        # 3) 왼쪽이 0이 되도록 패딩 (temp는 right->left 순서)
        while len(temp) < 4:
            temp.append(0)

        # 4) 행에 오른쪽부터 채우기
        for j in range(3, -1, -1):
            newgrid[i][j] = temp[3 - j]   # j=3(right) <- temp[0]

    for r in newgrid:
        print(*r)

def up(lst):
    newgrid = [[0]*4 for _ in range(4)]
    for j in range(4):
        # 1) 위 -> 아래로 0 아닌 값 모으기
        vals = []
        for i in range(4):
            if lst[i][j] != 0:
                vals.append(lst[i][j])

        # 2) 위쪽부터 합치기
        temp = deque()
        k = 0
        while k < len(vals):
            if k + 1 < len(vals) and vals[k] == vals[k+1]:
                temp.append(vals[k] * 2)
                k += 2
            else:
                temp.append(vals[k])
                k += 1

        # 3) 아래쪽에 0 채워서 길이 4 맞추기
        while len(temp) < 4:
            temp.append(0)

        # 4) 열에 위부터 채우기
        for i in range(4):
            newgrid[i][j] = temp[i]

    for r in newgrid:
        print(*r)

def down(lst):
    newgrid = [[0]*4 for _ in range(4)]
    for j in range(4):
        # 1) 아래 -> 위로 0 아닌 값 모으기 (bottom-first)
        vals = []
        for i in range(3, -1, -1):
            if lst[i][j] != 0:
                vals.append(lst[i][j])

        # 2) 아래쪽부터 합치기
        temp = deque()
        k = 0
        while k < len(vals):
            if k + 1 < len(vals) and vals[k] == vals[k + 1]:
                temp.append(vals[k] * 2)
                k += 2
            else:
                temp.append(vals[k])
                k += 1

        # 3) 위쪽이 0이 되도록 패딩 (temp는 bottom->top)
        while len(temp) < 4:
            temp.append(0)

        # 4) 열에 아래부터 채우기
        for i in range(3, -1, -1):
            newgrid[i][j] = temp[3 - i]  # i=3(bottom) <- temp[0]

    for r in newgrid:
        print(*r)

if dir == 'L':
    left(grid)
elif dir == 'R':
    right(grid)
elif dir == 'D':
    down(grid)
else:
    up(grid)