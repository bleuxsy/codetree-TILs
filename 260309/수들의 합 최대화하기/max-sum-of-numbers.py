def back(row, total):
    global answer

    if row == n:
        answer = max(answer, total)
        return

    for col in range(n):
        if not used[col]:
            used[col] = 1
            back(row + 1, total + grid[row][col])
            used[col] = 0


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

used = [0] * n
answer = 0

back(0, 0)
print(answer)