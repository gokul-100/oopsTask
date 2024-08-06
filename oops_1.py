class Student:
    gradution="btech"
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
        self.gradution="mtech"
        
    def Display(self):
        print(f'{self.firstname}{self.lastname}')
        
obj1=Student("gokul","kannan")
# obj2=Student("ajith","kumar")
# # print(obj1.firstname)
# obj1.Display()
# obj2.Display()

# Student.Display(self=obj2)
print(obj1.gradution) #it will call instance variable
print(obj1.__class__.gradution) #it will call class variable