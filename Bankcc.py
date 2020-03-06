class BankAccount:
    def __init__(self, first_name='m', last_name='k', account_num=67, balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_num = account_num
        self.balance = balance
        self.transactions = []
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
        
        
print("WELCOME TO THE ATM MACHINE")
    
pin = int(input("Enter your pin code:"))
correct_pin = 0000
count = 0
while pin != correct_pin and count<3:
    count +=1
    pin = int(input("Invalid Pin Code!!!!... Try Again:"))
    if count == 3 and pin != correct_pin:
        print("Session Ended")
        break
else:
        if count<4 and pin == correct_pin:
            print ("WELCOME")
            print("\n1 - Deposit  \t 2 - Withdraw \t 3 - Check Balance \t 4 - Exit ")  
        selection = int(input("\nEnter your selection:"))

# creating an object of clas
s=BankAccount 
s = BankAccount('mimi','dan',8871) 
s.deposit() 
s.withdraw() 
s.display() 