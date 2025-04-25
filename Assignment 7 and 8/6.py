'''Write a Python program to create a class representing a bank. Include methods for managing
customer accounts and transactions.'''
 
class Bank:
    def __init__(self,acc,name,bal):
        self.name=name
        self.acc=acc
        self.bal=bal
    def deposit(self):
        depo=int(input("enter the amount you want to deposit:"))
        self.bal+=depo
        print("Amount deposited succesfully")
        print(f"Your current balance={self.bal}")
    @property
    def current_bal(self):
        return self.bal
    def debit(self):
        n=int(input("enter the amount you want to debit:"))
        if (n>self.bal):
            print("Insufficient balance")
            return
        else:
            self.bal-=n
            print("Amount debited succesfully")
            print(f"Your current balance={self.bal}")
sup=Bank(1234,'mam',11000)  
print(f"Good morning {sup.name}")
ch=int(input("Enter your choice\n1.deposit\n2.withdrawl\n3.check balance\n"))
match ch:
    case 1:
        sup.deposit() 
    case 2:
        sup.debit()
    case 3:
        print(sup.current_bal)
print("Thank you..visit again")