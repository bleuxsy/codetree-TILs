import sys
input = sys.stdin.readline

n = int(input().rstrip())
grid = [list(input().rstrip()) for _ in range(n)]

pos = {}   # 숫자 위치 저장
nums = []  # 숫자 목록
sx = sy = ex = ey = -1

for i in range(n):
    for j in range(n):
        if grid[i][j].isdigit():
            num = int(grid[i][j])
            nums.append(num)
            pos[num] = (i, j)
        elif grid[i][j] == 'S':
            sx, sy = i, j
        elif grid[i][j] == 'E':
            ex, ey = i, j

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

nums.sort()

if len(nums) < 3:
    print(-1)
else:
    answer = sys.maxsize

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                a, b, c = nums[i], nums[j], nums[k]

                total = 0
                total += dist((sx, sy), pos[a])
                total += dist(pos[a], pos[b])
                total += dist(pos[b], pos[c])
                total += dist(pos[c], (ex, ey))

                answer = min(answer, total)

    print(answer if answer != sys.maxsize else -1)