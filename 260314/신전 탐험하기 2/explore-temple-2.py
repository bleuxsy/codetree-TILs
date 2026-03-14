n = int(input())
l, m, r = [], [], []

for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

INF = -10**18

# dp[s][i][d]
# s: 시작 방향 (0=왼, 1=중, 2=오)
# i: 현재 층
# d: i층에서 선택한 방향
dp = [[[INF] * 3 for _ in range(n + 1)] for _ in range(3)]

# 왼쪽에서 시작
dp[0][1][0] = l[0]
# 중간에서 시작
dp[1][1][1] = m[0]
# 오른쪽에서 시작
dp[2][1][2] = r[0]

for s in range(3):
    
    for i in range(2, n):
        dp[s][i][0] = max(dp[s][i - 1][1], dp[s][i - 1][2]) + l[i - 1]
        dp[s][i][1] = max(dp[s][i - 1][0], dp[s][i - 1][2]) + m[i - 1]
        dp[s][i][2] = max(dp[s][i - 1][0], dp[s][i - 1][1]) + r[i - 1]

# 마
dp[0][n][1] = max(dp[0][n - 1][0], dp[0][n - 1][2]) + m[n - 1]
dp[0][n][2] = max(dp[0][n - 1][0], dp[0][n - 1][1]) + r[n - 1]

dp[1][n][0] = max(dp[1][n - 1][1], dp[1][n - 1][2]) + l[n - 1]
dp[1][n][2] = max(dp[1][n - 1][0], dp[1][n - 1][1]) + r[n - 1]

#
dp[2][n][0] = max(dp[2][n - 1][1], dp[2][n - 1][2]) + l[n - 1]
dp[2][n][1] = max(dp[2][n - 1][0], dp[2][n - 1][2]) + m[n - 1]

answer = 0
for i in range(3):
    answer = max(answer, max(dp[i][n]))

print(answer)