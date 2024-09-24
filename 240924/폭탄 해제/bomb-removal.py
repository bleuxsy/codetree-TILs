class Solution:
    def __init__(self,code,color,seconds):
        self.code = code
        self.color = color
        self.seconds = seconds


code, color,seconds = tuple(input().split())
solution1 =Solution(code,color,seconds)
print('code :',solution1.code)
print('color :',solution1.color)
print('second :',solution1.seconds)