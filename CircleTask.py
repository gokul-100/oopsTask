class Circle :
    PI=3.14
    def __init__(self) -> None:
        self.radius=0.0
        self.Area=0.0
        self.circumference=0.0
        
    def accept(self):
        self.radius=int(input('enter the radius: '))
        
    def CalculateArea(self):
        self.Area=Circle.PI*self.radius*self.radius
        
    def Calculatecircumference(self):
        self.circumference=2*Circle.PI*self.radius
    
    def display(self):
        print("--------display the details-----------")
        print(f'radius of circle -> {self.radius}')
        print(f'area of circle -> {self.Area}')
        print(f'circumference of circle -> {self.circumference}')
        
ball=Circle()   
ball.accept()
ball.CalculateArea()
ball.Calculatecircumference()
ball.display()     