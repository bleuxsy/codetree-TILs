import heapq

INF = 10**18

def dijkstra(graph):
    dist = [INF] * (n + 1)
    pq = []
    dist[1] = 0
    heapq.heappush(pq, (0, 1))

    while pq:
        cur_dist, x = heapq.heappop(pq)

        if dist[x] < cur_dist:
            continue

        for nx, w in graph[x]:
            nd = cur_dist + w
            if dist[nx] > nd:
                dist[nx] = nd
                heapq.heappush(pq, (nd, nx))

    return dist[n]

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[] for _ in range(n + 1)]
for a, b, w in edges:
    grid[a].append((b, w))
    grid[b].append((a, w))

org = dijkstra(grid)

answer = org

for i in range(m):   # 간선 전체를 다 봐야 함
    new_grid = [[] for _ in range(n + 1)]

    for j in range(m):
        a, b, w = edges[j]
        if j == i:
            w *= 2
        new_grid[a].append((b, w))
        new_grid[b].append((a, w))

    new_dist = dijkstra(new_grid)
    answer = max(answer, new_dist)

print(answer - org)