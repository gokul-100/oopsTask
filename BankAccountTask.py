class BankAccount:
    ROI=10.5
    def __init__(self) -> None:
        self.name=""
        self.amount=0
    def accept(self):
        self.name=input("enter the name: ")
        self.amount=int(input("enter the amount: "))
        
    def Deposite(self):
        amount=int(input("enter the amount to deposite: "))
        if amount>0:
            self.amount+=amount
            print("amount deposited successfully........")
        else:
            print("you must enter the amount above 0")
    
    def withdraw(self):
        amount=int(input("enter the amount to withdraw: "))
        if self.amount>=amount:
            self.amount-=amount
            print("amount withdraw successfully.....")
        else:
            print("insufficent amount ......")
        
    def CalculateInterest(self):
        intrest=(BankAccount.ROI*self.amount)/100
        print(f'intrest of these amount is {intrest}')
        
PERSON1=BankAccount()
PERSON1.accept()
PERSON1.Deposite()
PERSON1.withdraw()
PERSON1.CalculateInterest()
