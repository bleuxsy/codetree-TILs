class Worker:
    def __init__(self, level='', score=0):
        self.level = level
        self.score = int(score)  # 점수를 정수로 변환
    
workers = []

# 5명의 요원 정보를 입력받아 Worker 객체를 리스트에 추가
for i in range(5):
    level, score = input().split()  # 입력을 level과 score로 나눔
    workers.append(Worker(level, score))

# 점수를 기준으로 요원 리스트를 정렬
workers.sort(key=lambda x: x.score)

# 점수가 제일 낮은 요원 출력
minworker = workers[0]
print(minworker.level, minworker.score)