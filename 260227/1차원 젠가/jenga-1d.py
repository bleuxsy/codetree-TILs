n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

def move(lst):
    temp = []
    for i in range(len(lst)):
        if lst[i] != 0:
            temp.append(lst[i])
  
    return temp


#첫번째 제거
for i in range(s1-1, e1):
    # 0으로 변경하기
    blocks[i] = 0
blocks2 = move(blocks)


for i in range(s2-1, e2):
    blocks2[i]=0

answer = move(blocks2)
print(len(answer))
for a in answer:
    print(a)
