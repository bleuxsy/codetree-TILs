import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

a, b = map(int, input().split())
INF = 10**18
path = [0] * (n + 1)
D = [INF] * (n + 1)
pq = []
graph = [[] for _ in range(n + 1)]

for x, y, w in edges:
    graph[x].append((y, w))
    graph[y].append((x, w))

D[a] = 0
heapq.heappush(pq, (0, a))
visited = [False] * (n + 1)

while pq:
    cw, cx = heapq.heappop(pq)

    if visited[cx]:
        continue
    visited[cx] = True

    for nx, nw in graph[cx]:
        if D[nx] > D[cx] + nw:
            D[nx] = D[cx] + nw
            path[nx] = cx
            heapq.heappush(pq, (D[nx], nx))

if D[b] == INF:
    print(-1)
else:
    answer = []
    x = b
    while x != 0:
        answer.append(x)
        if x == a:
            break
        x = path[x]

    print(D[b])
    print(*answer[::-1])