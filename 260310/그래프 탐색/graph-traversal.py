def dfs(v):
    for nxt in graph[v]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

visited[1] = True
dfs(1)

print(sum(visited) - 1)