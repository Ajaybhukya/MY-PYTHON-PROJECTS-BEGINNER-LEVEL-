balance=0
transactions=[]
users={123:2233}
def users_adding(userid,pin):
    if userid not in users.keys():
        users.update({userid:pin})
        print('Account created you can login')
    else:
        print('Account already exists')
        print('Please login')
def exisist_user(userid):
    if userid in users.keys():
        return True
    else:
        return False
def withdraw(amount):
    global balance
    if balance<amount:
        return "Insufficient funds"
    else:
        balance=balance-amount
        transactions.append("Withdrawed:"+ str(amount))
        return "Amount withdrawn:"+str(balance)
def deposit(amount):
    global balance
    balance=balance+amount
    transactions.append("Deposited:"+ str(amount))
    return "After deposit amount "+str(balance)
print('1.New user')
print('2.Exisisted user')
choice=int(input('Enter your choice: '))
if choice==1:
    userid=int(input("Enter your userid: "))
    pin=int(input("Enter your pin: "))
    users_adding(userid,pin)
else:
    print("Login in with exsisted userid and pin")
userid = int(input("Enter your userid: "))
pin = int(int(input("Enter your pin: ")))
if exisist_user(userid)==True:
    while True:
        print("welcome to our ATM")
        print("1.Deposit")
        print("2.Withdrawal")
        print("3.history")
        print("4.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            amount=int(input("Enter amount to deposit   :"))
            if amount<=0:
                print("Invalid amount")
            else:
                print(deposit(amount))
        elif ch==2:
            amount=int(input("Enter amount to deposit   :"))
            if amount<=0:
                print("Invalid amount")
            else:
                print(withdraw(amount))
        elif ch==3:
         if not transactions:
             print("No transactions are available")
         else:
            print("The transactions are :")
            for i in transactions:
                print(i)
        elif ch==4:
            print("Thank you for using our ATM")
            break
        else:
            print("Invalid choice re-enter")
else:
    print("Invalid userid or pin")