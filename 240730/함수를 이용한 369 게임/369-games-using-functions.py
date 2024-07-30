def contains_369(n):
    while n > 0:
        if n%10 ==3 or n%10 == 6 or n%10 == 9:
            return True
        n//=10
    return False
def is_369_number(n):
    return contains_369(n) or n%3 == 0

a,b = map(int,input().split())
cnt = 0
for num in range(a,b+1):
    if is_369_number(num):
        cnt+=1
print(cnt)