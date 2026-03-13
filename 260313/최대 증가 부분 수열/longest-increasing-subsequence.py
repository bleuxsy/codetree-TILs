n = int(input())
m = list(map(int, input().split()))
dp = [1] * n
# Please write your code here.
for i in range(1, n):
    for j in range(0, n):
        if m[i] > m[j]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))