def move(ladder, start):
    col = start
    for r in range(m):
        if col < n - 1 and ladder[r][col] == 1:
            col += 1
        elif col > 0 and ladder[r][col - 1] == 1:
            col -= 1
    return col


def check(new_ladder):
    for num in range(n):
        end = move(new_ladder, num)
        if gold[num] != end:
            return False
    return True


def make(idx, new_ladder, total):
    global answer

    # 이미 최솟값보다 많이 썼으면 중단
    if total >= answer:
        return

    # 모든 가로줄을 다 본 경우
    if idx == m:
        if check(new_ladder):
            answer = min(answer, total)
        return

    # 1) 현재 가로줄을 선택하지 않는 경우
    make(idx + 1, new_ladder, total)

    # 2) 현재 가로줄을 선택하는 경우
    i, j = edges[idx]          # i: 세로줄 번호, j: 행 번호
    row = j - 1
    col = i - 1

    new_ladder[row][col] = 1
    make(idx + 1, new_ladder, total + 1)
    new_ladder[row][col] = 0


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

ladder = [[0] * (n - 1) for _ in range(m)]
gold = [0] * n

for i, j in edges:
    ladder[j - 1][i - 1] = 1

for num in range(n):
    gold[num] = move(ladder, num)

answer = m
make(0, [[0] * (n - 1) for _ in range(m)], 0)

print(answer)