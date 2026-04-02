import sys
import heapq

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

dist = [0] * (n + 1)

# 그래프를 인접행렬로 표현
# 양방향 그래프이므로 양쪽 다 표시해줍니다.
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x][y] = z
    graph[y][x] = z


def dijkstra(k):
    # 그래프에 있는 모든 노드들에 대해
    # 초기값을 전부 아주 큰 값으로 설정
    for i in range(1, n + 1):
        dist[i] = INT_MAX

    # 시작위치에는 dist값을 0으로 설정
    dist[k] = 0

    # visited 값을 초기화해줍니다.
    for i in range(1, n + 1):
        visited[i] = False

    pq = []
    heapq.heappush(pq, (0, k))

    # heapq를 이용한 다익스트라
    while pq:
        min_dist, min_index = heapq.heappop(pq)

        if visited[min_index]:
            continue

        visited[min_index] = True

        # 최솟값에 해당하는 정점에 연결된 간선들을 보며
        # 시작점으로부터의 최단거리 값을 갱신해줍니다.
        for j in range(1, n + 1):
            # 간선이 존재하지 않는 경우에는 넘어갑니다.
            if graph[min_index][j] == 0:
                continue

            if dist[j] > dist[min_index] + graph[min_index][j]:
                dist[j] = dist[min_index] + graph[min_index][j]
                heapq.heappush(pq, (dist[j], j))


dijkstra(n)

# 도착지에서 시작하여
# 시작점이 나오기 전까지
# 최단거리를 만족하는 경로 중
# 가장 간선 번호가 작은 곳으로 이동합니다.
x = 1
vertices = []
vertices.append(x)
while x != n:
    for i in range(1, n + 1):
        # 간선이 존재하지 않는 경우에는 넘어갑니다.
        if graph[i][x] == 0:
            continue

        # 만약 b -> ... -> i -> x ... -> a로
        # 실제 최단거리가 나올 수 있는 상황이었다면
        # i를 작은 번호부터 보고 있으므로
        # 바로 선택해줍니다.
        if dist[i] + graph[i][x] == dist[x]:
            x = i
            break

    vertices.append(x)

# A가 이동한 최단거리에서
# 사전순으로 가장 앞선 경로상에 있는
# 간선을 제거합니다.
length = len(vertices)
for i in range(length - 1):
    x = vertices[i]
    y = vertices[i + 1]
    graph[x][y] = 0
    graph[y][x] = 0

# B가 이동했을 때의
# 최단거리를 구합니다.
dijkstra(1)

ans = dist[n]
# 불가능하다면 -1을 출력합니다.
if ans == INT_MAX:
    ans = -1

print(ans)