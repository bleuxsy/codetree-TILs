n = int(input())

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = 2
if n >= 2:
    dp[2] = 7

for i in range(3, n + 1):
    dp[i] = 3* dp[i - 1] +1

print(dp[n]%1000000007)