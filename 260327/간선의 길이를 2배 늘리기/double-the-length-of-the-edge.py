
# Please write your code here.
"""

양방향
한 개의 간선을 골라 길이를 2배늘려서 1 - N까지 도달하는 데의 최단거리를 최대
2배 늘리기전과 후의 차이 출력




5 7
2 1 5
1 3 1
3 2 8
3 5 7
3 4 3
2 4 7
4 5 2


"""
import heapq
def dijkstra(graph):
    visited = [False] * (n+1)
    B = [INF] * (n+1)
    pq = []
    heapq.heappush(pq, (0 , 1))
    # 시작점은 1
    B[1] = 0

    while pq:
        w, sx = heapq.heappop(pq)

        if visited[sx] :
            continue
        visited[sx] = True

        for nx, nw in graph[sx]:
            if B[nx] > B[sx] + nw:
                B[nx] = B[sx] + nw
                heapq.heappush(pq, (B[nx], nx))



    return B[n]
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]


INF = 10**18
grid = [[] for _ in range(n+1)]
for x, y, w in edges:
    grid[x].append((y, w))
    grid[y].append((x, w))


answer = 0
org = dijkstra(grid)
for i in range(1, n+1):
    new_grid = [[] for _ in range(n+1)]
    for j in range(m):
        a, b, w = edges[j]
        if j == i:
            w*= 2
        new_grid[a].append((b,w))
        new_grid[b].append((a,w))

    new = dijkstra(new_grid)
    answer = max(answer, new)

print(answer - org)
