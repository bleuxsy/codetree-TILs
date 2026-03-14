n = int(input())
MAX = 10**9 + 7

dp = [[0] * (n + 1) for _ in range(3)]

if n >= 1:
    dp[0][1] = 1
    dp[1][1] = 1
    dp[2][1] = 1

if n >= 2:
    dp[0][2] = 3
    dp[1][2] = 3
    dp[2][2] = 3

for i in range(3, n + 1):
    # Good
    dp[0][i] = (dp[0][i-1] + dp[1][i-1] + dp[2][i-1]) % MAX

    # Bad
    dp[1][i] = (dp[0][i] - pow(2, i-3, MAX)) % MAX

    # Te
    if i >= 4:
        dp[2][i] = (dp[0][i] - ((i-1)*(i-2) * pow(2, i-4, MAX))) % MAX
    else:
        dp[2][i] = dp[0][i] % MAX

answer = (dp[0][n] + dp[1][n] + dp[2][n]) % MAX
print(answer)