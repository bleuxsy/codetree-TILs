def palindrome(mylist):
    if mylist == mylist[::-1]:
        return True
    return False

_list = str(input())
if palindrome(_list):
    print("Yes")
else:
    print("No")