N, K,T = input().split()

mylist =[]
for i in range(int(N)):
    word = input()
    if T in word:
        mylist.append(word)
mylist.sort()
print(mylist[int(K)-1])