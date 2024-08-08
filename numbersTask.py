# 5)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self) :
        self.value=int(input("enter the number "))
    
    def ChkPrime(self):
        if self.value>1:
            for i in range(2,self.value):
                if self.value%2==0:
                    print("not prime")
                    break
                else:
                    print("prime")
        else:
            print("not prime")

    def factors(self):
        print(f'factors of number {self.value} is : ')
        for i in range(1,self.value):
            if self.value%i==0:
                print(i,end=" ")
        print()
                
    
    def sumFactors(self):
        sum=0
        for i in range(1,self.value):
            if self.value%i==0:
                sum=sum+i
        return sum

    def ChkPerfect(self):
        if self.sumFactors()==self.value:
            print(f"{self.value} is perfect number")
        else:
            print(f"{self.value} is not perfect number")

num=Numbers()
num.ChkPerfect()
num.ChkPrime()
num.factors()
print(f'sum of factors is {num.sumFactors()}')
        

    
