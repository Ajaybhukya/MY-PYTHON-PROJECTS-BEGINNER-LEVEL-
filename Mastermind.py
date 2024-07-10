import random
num=random.randint(1000,10000)
print("Lets play mindmaster")
value=int(input("Enter a 4 digit value:"))
if value not in range(1000,10000):
    print("Invalid number")
    exit(0)
count=0
sn=str(num)
if value==num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    while True:
        correct=[]
        count+=1
        correct_choice=0
        sv=str(value)
        if sv==sn:
            print("You've become a Mastermind.")
            print("It took you only",count," tries.")
            break
        for i in range(0,4):
            if sv[i]==sn[i]:
                correct.append(sv[i])
                correct_choice+=1
            else:
                correct.append('X')
        if correct_choice>0:
            print("Not quite the number. But you did get",correct_choice,"digit(s) correct!")
            print("Also these numbers in your input were correct.")
            print("".join(correct))
        else:
            print("Never lose hope try again")
        option=input("Do you want to continue:yes/no:").lower()
        if option=='yes':
            value=int(input("Enter your next choice of numbers:"))
            continue
        else:
            print("Try again! invalid input ")
            break