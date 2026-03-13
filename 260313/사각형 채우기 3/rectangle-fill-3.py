MOD = 1000000007

n = int(input())

dp = [0] * (max(3, n + 1))
dp[0] = 1
dp[1] = 2
dp[2] = 7

for i in range(3, n + 1):
    dp[i] = (3 * dp[i - 1] + dp[i - 2] - dp[i - 3]) % MOD

print(dp[n])