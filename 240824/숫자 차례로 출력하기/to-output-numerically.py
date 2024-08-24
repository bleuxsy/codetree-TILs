def print_ascending(N):
    if N == 0:  # 재귀 종료 조건
        return
    print_ascending(N - 1)  # N-1까지 출력
    print(N,end=" ")  # 현재 N 출력

def print_descending(N):
    if N == 0:  # 재귀 종료 조건
        return
    print(N, end = " ")  # 현재 N 출력
    print_descending(N - 1)  # N-1까지 출력

# N 입력 받기
N = int(input())

# 1부터 N까지 출력
print_ascending(N)
print()

# N부터 1까지 출력
print_descending(N)