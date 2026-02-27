# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]
from collections import deque
# Read direction
dir = input()
def left(lst):
    for l in lst:
        temp = deque()
        i = 0
        l.append(0)
        while i < len(l)-1 :
            if l[i] == 0:
                i += 1
                continue
            if l[i] == l[i+1]:
                temp.append(2*l[i])
                i += 2
            else:
                temp.append(l[i])
                i += 1
        while len(temp) < 4:
            temp.append(0)
        print(*temp)
def right(lst):
    for l in lst:
        temp = deque()
        i = 3
        
        while i > -1  :
            if l[i] == 0:
                i -= 1
                continue
            if i == 0:
                temp.appendleft(l[i])
                break
            if l[i] == l[i-1]:
                temp.appendleft(2*l[i])
                i -= 2
            else:
                temp.appendleft(l[i])
                i -= 1
        while len(temp) < 4:
            temp.appendleft(0)
        print(*temp)
def up(lst):
    newgrid = list([0]*4 for _ in range(4))
    for j in range(4):
        i = 0
        temp = deque()
        
        while i <= 3 :
            if lst[i][j] == 0:
                    i += 1
                    continue
            if i == 3:
                temp.append(lst[i][j])
                break
            if lst[i][j]== lst[i+1][j]:
                    temp.append(2*lst[i][j])
                    i += 2
            else:
                    temp.append(lst[i][j])
                    i += 1
        while len(temp) < 4:
                temp.append(0)
        for i in range(4):
            newgrid[i][j] = temp[i]
    for r in newgrid:
        print(*r)
def down(lst):
    newgrid = [[0]*4 for _ in range(4)]

    for j in range(4):
        # 1) 아래 -> 위로 0 아닌 값만 모으기 (bottom-first)
        vals = []
        for i in range(3, -1, -1):
            if lst[i][j] != 0:
                vals.append(lst[i][j])

        # 2) 아래쪽부터 합치기 (bottom-first merge)
        temp = deque()
        k = 0
        while k < len(vals):
            if k + 1 < len(vals) and vals[k] == vals[k + 1]:
                temp.append(vals[k] * 2)
                k += 2
            else:
                temp.append(vals[k])
                k += 1

        # 3) 아래로 밀기: 부족한 건 위쪽이 0이 되도록 뒤에 0 추가 (temp는 bottom->top)
        while len(temp) < 4:
            temp.append(0)

        # 4) newgrid에 아래부터 채우기
        for i in range(3, -1, -1):
            newgrid[i][j] = temp[3 - i]   # i=3(bottom) <- temp[0]

    for r in newgrid:
        print(*r)
                
if dir == 'L':
    left(grid)

elif dir == 'R':
    right(grid)
    #down(grid)
elif dir == 'D':
    down(grid)
else:
    up(grid)