N, M = map(int, input().split())
nums = list(map(int, input().split()))


dp = [[0] * 41 for _ in range(N + 1)]

if -20 <= nums[0] <= 20:
    dp[1][nums[0] + 20] += 1
if -20 <= -nums[0] <= 20:
    dp[1][-nums[0] + 20] += 1


for i in range(1, N):
    x = nums[i]
    for v in range(41):
        if dp[i][v] > 0:
            cur = v - 20

            if -20 <= cur + x <= 20:
                dp[i + 1][cur + x + 20] += dp[i][v]

            if -20 <= cur - x <= 20:
                dp[i + 1][cur - x + 20] += dp[i][v]

print(dp[N][M + 20])