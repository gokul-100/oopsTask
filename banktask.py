class account:
    BankName='indian bank'
    RoI_On_fd=0
    def __init__(self) -> None:
        self.name=""
        self.amount=0
        self.Address=""
        self.Acc_no=0
    def creatingAcc(self):
        print('--------------------------creating the account----------------------------------')
        self.name=input("enter the name ")
        self.Amount=int(input("enter the amount "))
        self.Address=input('enter the address ')
        self.Acc_no=int(input('enter the account number '))
        
    def displayAccountInfo(self):
        print("----------------------------display the account info----------------------------")
        print(f'name of accountant {self.name}')
        print(f'amount in the account {self.Amount}')
        print(f'address->{self.Address}')
        print(f'account no {self.Acc_no}')
       
    def displayBankInfo(cls):
        print("bank name",cls.BankName)
        print("ROI_ON_FD",cls.RoI_On_fd)
        
def main():
    user1=account()
    user1.creatingAcc()
    user1.displayAccountInfo()
    account.displayBankInfo=classmethod(account.displayBankInfo)
    account.displayBankInfo()
    
    
    
if __name__=="__main__":
    main()
    
    