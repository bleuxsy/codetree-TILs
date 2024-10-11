def print_recursive(N):
    if N == 0:
        return
    # N부터 1까지 출력
    print(N, end=' ')
    print_recursive(N - 1)
    # 다시 1부터 N까지 출력
    print(N, end=' ')

# 입력 받기
N = int(input())

# 함수 호출
print_recursive(N)