class addOvrld:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        a=self.a+other.a
        b=self.b+other.b
        return addOvrld(a,b)
    def display(self):
        print("a is:",self.a)
        print("b is:",self.b)
o1 = addOvrld(2,3)
o2 = addOvrld(2,2)
o3 = addOvrld(8,5)
obj=o1+o2+o3
obj.display()
