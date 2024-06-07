import sys
class Bank:
 def __init__(self,name, balance=0.0):
  self.name=name
  self.balance=balance
 def deposit(self, amount):
  self.balance+=amount
  return self.balance
 def withdraw(self, amount):
  if amount>self.balance:
   print("Insufficient funds")
  else:
   self.balance-=amount
   return self.balance
 def amount(self):
  return self.balance
name=input("Enter your name\n")
b=Bank(name)
print("Bank services are")
while(True):
 print("__MENU__")
 print("1.deposit")
 print("2.withdraw")
 print("3.balance enquiry")
 print("4.exit")
 ch=int(input("Read your service"))
 if ch==1:
  amt=int(input("Enter your amount\n"))
  print("After deposit amount:",b.deposit(amt))
 elif ch==2:
  amt=int(input("Enter your amount\n"))
  print("After withdraw amount:",b.withdraw(amt))
 elif ch==3:
  print("Amount=",b.amount())
 else:
  print("Thank you")
  sys.exit()