S = input()
P = input()
flag =  'false'
# Please write your code here.
for p in range(len(P)):
    if p >= len(S):
        break
    else:
        if P[p] == '.':
            flag = 'true'
            continue
        elif P[p] == '*':
            break
        
        elif P[p] == S[p]:
            flag = 'true'
    
print(flag)
    
        