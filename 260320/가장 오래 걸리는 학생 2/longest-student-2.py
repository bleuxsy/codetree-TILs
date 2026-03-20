import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

INF = float('inf')
D = [INF] * (n + 1)

# 간선 반대로 저장
graph = [[] for _ in range(n + 1)]
for a, b, d in edges:
    graph[b].append((a, d))

pq = []
heapq.heappush(pq, (0, n))
D[n] = 0

while pq:
    sw, idx = heapq.heappop(pq)

    if sw > D[idx]:
        continue

    for ny, nw in graph[idx]:
        if sw + nw < D[ny]:
            D[ny] = sw + nw
            heapq.heappush(pq, (D[ny], ny))

print(max(D[1:n]))