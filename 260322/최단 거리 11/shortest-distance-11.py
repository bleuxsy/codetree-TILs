import heapq

INF = 10**18

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cw, cx = heapq.heappop(pq)

        if cw > dist[cx]:
            continue

        for nx, nw in graph[cx]:
            nd = cw + nw
            if dist[nx] > nd:
                dist[nx] = nd
                heapq.heappush(pq, (nd, nx))

    return dist


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for x, y, w in edges:
    graph[x].append((y, w))
    graph[y].append((x, w))

for i in range(1, n + 1):
    graph[i].sort()   # 번호 작은 정점부터 보려고 정렬

distA = dijkstra(a, graph, n)
distB = dijkstra(b, graph, n)

if distA[b] == INF:
    print(-1)
else:
    route = [a]
    cur = a

    while cur != b:
        for nxt, w in graph[cur]:
            if distA[cur] + w + distB[nxt] == distA[b]:
                route.append(nxt)
                cur = nxt
                break

    print(distA[b])
    print(*route)