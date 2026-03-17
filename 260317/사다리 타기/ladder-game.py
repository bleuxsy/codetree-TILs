def move(ladder, start):
    col = start
    for r in range(H):
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

    if total >= answer:
        return

    if idx == m:
        if check(new_ladder):
            answer = min(answer, total)
        return

    # 선택 안 함
    make(idx + 1, new_ladder, total)

    # 선택 함
    i, j = edges[idx]
    row = j - 1
    col = i - 1

    new_ladder[row][col] = 1
    make(idx + 1, new_ladder, total + 1)
    new_ladder[row][col] = 0


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

H = max(j for i, j in edges) if edges else 0

ladder = [[0] * (n - 1) for _ in range(H)]
gold = [0] * n

for i, j in edges:
    ladder[j - 1][i - 1] = 1

for num in range(n):
    gold[num] = move(ladder, num)

answer = m
make(0, [[0] * (n - 1) for _ in range(H)], 0)

print(answer)