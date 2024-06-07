def check_balance(balance):
 print("your balance is", balance)
def deposit(balance, amount):
  balance+=amount
  return balance
def withdraw(balance, amount):
    if amount>balance:
        print("insufficient balance")
    else:
        balance-=amount
        print(f"{amount} withdraw successfully")
        return balance 
while True:
    print("1.check balance")          
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
#while True:    
    ch=int(input("enter your choice"))
if ch==1:
    check_balance(balance)     
elif ch==2:
    amount=int(input("enter your deposited amount:"))
    balance =deposit(balance, amount)    
elif ch==3:
    amount=int(input("enter your withdraw money:"))    
    balance =withdraw(balance, amount)
else:
    print("thank you")    