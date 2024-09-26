class Boxes : 
    def __init__(self, name="codetree", code="50"):
        self.name= name
        self.code = code
boxes1 = Boxes()
name1,code1= input().split()
boxes2 = Boxes(name1,code1)
print(f'product {boxes1.code} is {boxes1.name}')
print(f'product {boxes2.code} is {boxes2.name}')