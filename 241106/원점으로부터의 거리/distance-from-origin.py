class Point:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        # 원점에서의 맨해튼 거리 계산
        self.distance = abs(x) + abs(y)

# 점의 개수 입력
N = int(input())
points = []

# 점의 좌표와 번호를 입력받아 저장
for i in range(N):
    x, y = map(int, input().split())
    points.append(Point(x, y, i + 1))

# 맨해튼 거리 기준으로 정렬, 거리가 같을 경우 번호가 작은 순서로 정렬
points.sort(key=lambda point: (point.distance, point.index))

# 정렬된 결과의 번호를 출력
for point in points:
    print(point.index)