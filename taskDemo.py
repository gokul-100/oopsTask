class Demo:
    
    def __init__(self,num1,num2):
        self.val1=num1
        self.val2=num2
    def fun(self):
        print(f'{self.val1},{self.val2} this is fun method calling')
    def gun(self):
        print(f'{self.val1},{self.val2} this is gun method calling' )

Obj1 =Demo(11,21)
Obj2 = Demo(51,101)

Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj2.gun()
print(Obj1.value)