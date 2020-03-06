class MomoAccount:
    def __init__(self, first_name, last_name, account_num, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_num = account_num
        self.balance = balance
        self.transactions = []
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
    def withdrawal(self, amount, limit=1000):
        if self.balance - amount > 0 and amount <= limit:
            amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
        
        
print("Hello There")
            

m=MomoAccount 
m = MomoAccount('mimi','dan',8871) 
m.deposit() 
m.withdraw() 
m.display()     
