# 입력 문자열과 목적 문자열을 받습니다.
input_string = input().strip()
target_string = input().strip()

# 목적 문자열이 입력 문자열의 부분 문자열로 존재하는 경우 그 시작 인덱스를 출력
index = input_string.find(target_string)

# 인덱스를 출력합니다. (존재하지 않을 경우 -1이 출력됩니다.)
print(index)