def dfs(weight, total):
    global answer

    answer = max(answer, total)

    for i in range(N):
        if not visited[i]:
            nxtw = weight + w[i]
            nxtv = total + v[i]

            if nxtw <= M and dp[weight] + v[i] > dp[nxtw]:
                visited[i] = 1
                dp[nxtw] = dp[weight] + v[i]
                dfs(nxtw, nxtv)
                visited[i] = 0


N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

dp = [0] * (M + 1)
visited = [0] * N
answer = 0

dfs(0, 0)
print(answer)