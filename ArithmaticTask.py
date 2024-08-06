class numbers:
    def __init__(self) -> None:
        self.val1=0
        self.val2=0

    def accept(self):
        self.val1=int(input("enter the value 1 : "))
        self.val2=int(input("enter the value 2 : "))

    def Addition(self):
        return self.val1+self.val2
    def subtraction(self):
        return self.val1-self.val2
    def multiplication(self):
        return self.val1*self.val2
    def divison(self):
        return self.val1/self.val2
    
obj1=numbers()
obj1.accept()
print("Addition of two values are",obj1.Addition())
print("divison of two values are",obj1.divison())
print("multiplication of two values are",obj1.multiplication())
print("subtraction of two values are",obj1.subtraction())
