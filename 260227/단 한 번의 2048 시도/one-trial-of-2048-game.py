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
    newgrid = list([0]*4 for _ in range(4))
    for j in range(4):
        i = 3
        temp = deque()
        
        while i >= 0 :
            if lst[i][j] == 0:
                    i -= 1
                    continue
            if i == 0:
                temp.appendleft(lst[i][j])
                break
            if lst[i][j]== lst[i-1][j]:
                    temp.appendleft(2*lst[i][j])
                    i -= 2
            else:
                    temp.append(lst[i][j])
                    i -= 1
        while len(temp) < 4:
                temp.appendleft(0)
        for i in range(4):
            newgrid[i][j] = temp[i]
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