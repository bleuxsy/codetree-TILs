import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 폭탄 위치 저장
bombs = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))

max_area = 0


def first(board, x, y):
    for i in range(x - 2, x + 3):
        if 0 <= i < n:
            board[i][y] = 1


def second(board, x, y):
    board[x][y] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] = 1


def third(board, x, y):
    board[x][y] = 1
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] = 1


def dfs(idx, board):
    global max_area

    if idx == len(bombs):
        # 1의 개수 세기
        count = sum(sum(row) for row in board)
        max_area = max(max_area, count)
        return

    x, y = bombs[idx]

    # 3가지 선택지
    for bomb_type in range(3):
        new_board = copy.deepcopy(board)

        if bomb_type == 0:
            first(new_board, x, y)
        elif bomb_type == 1:
            second(new_board, x, y)
        else:
            third(new_board, x, y)

        dfs(idx + 1, new_board)


dfs(0, grid)

print(max_area)