n = int(input())
MAX = 10**9 + 7

# Please write your code here.
dp = [[0] *(n+1) for _ in range(3)]

dp[0][1] = 1
dp[1][1] = 1
dp[2][1] = 1

dp[0][2] = 3
dp[1][2] = 3
dp[2][2] = 3

for i in range(3,n+1):
    # Good
    dp[0][i] = dp[0][i-1] + dp[1][i-1] + dp[2][i-1]
    # Bad
    dp[1][i] = dp[0][i] - 2 ** (i-3)
    # Te
    dp[2][i] = dp[0][i] - ((i-1)*(i-2)* 2**(i-4))

   
print(int((dp[0][n] + dp[1][n] + dp[2][n])%MAX))