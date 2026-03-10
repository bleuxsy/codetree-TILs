
def dfs(x, y):
    people = 1
    
    for dx, dy in  [(-1, 0), (1, 0 ), (0, 1), (0 , -1)]:
        nx, ny = x + dx , y + dy
        if 0<= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                
                people += dfs(nx, ny)
                
    
    return people 

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
peoples = []
town = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            visited[i][j] = True
            peoples.append(dfs(i, j))

print(len(peoples))
peoples.sort()
for p in peoples:
    print(p)
# Please write your code here.
# 1. dfs
# 2. 1인 곳에서 시작해서 갈 곳 없으면 people 수 저장 . town + 1
