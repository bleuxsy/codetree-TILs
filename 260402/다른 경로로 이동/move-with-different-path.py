import heapq

INF = 10**18

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


def dijkstra(start, blocked):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, x = heapq.heappop(pq)

        if dist[x] < d:
            continue

        for nx, w in graph[x]:
            if (x, nx) in blocked:
                continue

            nd = d + w
            if dist[nx] > nd:
                dist[nx] = nd
                heapq.heappush(pq, (nd, nx))

    return dist


# 1번에서의 최단거리
blocked = set()
dist1 = dijkstra(1, blocked)

# N번에서의 최단거리
distN = dijkstra(n, blocked)

# A가 못 가면 끝
if dist1[n] == INF:
    print(-1)
    exit()

# A의 사전순 최단경로 복원
cur = 1
while cur != n:
    candidates = []

    for nx, w in graph[cur]:
        # cur -> nx가 최단경로 위에 있는지 확인
        if dist1[cur] + w + distN[nx] == dist1[n]:
            candidates.append(nx)

    nxt = min(candidates)   # 사전순으로 가장 앞선 정점 선택
    blocked.add((cur, nxt))
    blocked.add((nxt, cur))
    cur = nxt

# B의 최단거리
distB = dijkstra(1, blocked)

print(-1 if distB[n] == INF else distB[n])