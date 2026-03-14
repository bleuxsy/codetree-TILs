S = input().strip()
P = input().strip()

n = len(S)
m = len(P)

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][0] = True

# 빈 문자열과 패턴 매칭 처리
for j in range(2, m + 1):
    if P[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 일반 문자 또는 '.'
        if P[j - 1] == '.' or P[j - 1] == S[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        # '*'
        elif P[j - 1] == '*':
            # 앞 문자를 0번 사용하는 경우
            dp[i][j] = dp[i][j - 2]

            # 앞 문자를 1번 이상 사용하는 경우
            if P[j - 2] == '.' or P[j - 2] == S[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]

print('true' if dp[n][m] else 'false')