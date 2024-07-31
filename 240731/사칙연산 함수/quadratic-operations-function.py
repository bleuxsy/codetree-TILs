def summ(x,y):
    return (x+y)
def minus(x,y):
    return (x-y)
def mul(x,y):
    return(x*y)
def remind(x,y):
    return(x//y)

result = 0
a, o, c= input().split()
if o =="+":
    result = summ(int(a),int(c))
    print(a,o,c,"=",result,end=" ")
elif o =="-":
   result=  minus(int(a),int(c))
   print(a,o,c,"=",result,end=" ")
elif o =="*":
    result = mul(int(a),int(c))
    print(a,o,c,"=",result,end=" ")
elif o =="/":
    result = remind(int(a),int(c))
    print(a,o,c,"=",result,end=" ")
else:
    print("false")