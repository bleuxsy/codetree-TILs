def notyoon(y):
    if y%4 ==0 :
        if y%100 == 0:
            if y%400 == 0:
                return False
            return True
        return False
    return True
def isMonth(y,m,d):
    if m in [1,3,5,7,8,10,12]:
        if d <32:
            return True
        return False
    if m in [2,4,6,9,11]:
        if d<31 : 
            return True
        return False
    if m == 2:
        if notyoon(y) and d < 29: 
            return True
        if notyoon(y)==False and d<30:
            return True
        return False

Y, M, D = map(int, input().split())
if isMonth(Y,M,D):
    if M in [3,4,5]:
        print("Spring")
    elif M in [6,7,8]:
        print("Summer")
    elif M in [9,10,11]:
        print("Fall")
    else :
        print("Winter")
else:
    print(-1)