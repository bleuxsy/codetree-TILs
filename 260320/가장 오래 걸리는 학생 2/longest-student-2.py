import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INF = float('inf')
# Please write your code here.
D = [INF] * (n+1)

""" 
    학교에서 각 지점으로 다익스트라 시켜야 함.
    간선 방향을 반대로 바꿔야 함. 

"""

grid = [[INF] * (n+1) for _ in range(n+1)]


pq = []


for edge in edges:
    grid[edge[1]][edge[0]] = edge[2]

grid[5][5] = 0
visited = ([False] * (n+1))
heapq.heappush(pq, (0, n))
D[n] = 0
while pq:
    sw, idx = heapq.heappop(pq)
    if visited[idx]:
        continue
    visited[idx] = True

    for ny, nw in enumerate(grid[idx]):
        if nw == INF :
            continue

        if  sw + nw < D[ny]:

            D[ny] = sw +nw
            
            heapq.heappush(pq, (D[ny], ny))

print(max(D))


