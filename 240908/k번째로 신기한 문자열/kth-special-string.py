# 입력 받기
N, K, T = input().split()

# 단어를 저장할 리스트
mylist = []

# N개의 단어 입력 받기
for i in range(int(N)):
    word = input()
    # 단어가 T로 시작하는 경우 리스트에 추가
    if word.startswith(T):
        mylist.append(word)

# 사전 순으로 정렬
mylist = sorted(mylist)

# K번째 단어 출력 (1-based index 이므로 K-1 사용)
print(mylist[int(K)-1])