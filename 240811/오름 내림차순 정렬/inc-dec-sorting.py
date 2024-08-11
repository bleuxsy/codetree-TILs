n = int(input())  
elements = list(map(int, input().split()))  # 두 번째 줄에서 n개의 원소를 공백을 기준으로 구분하여 입력 받습니다.


asc_sorted = sorted(elements)


desc_sorted = sorted(elements, reverse=True)

print(' '.join(map(str, asc_sorted)))
print(' '.join(map(str, desc_sorted)))