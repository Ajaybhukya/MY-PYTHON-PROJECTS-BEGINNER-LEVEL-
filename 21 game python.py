"""
Rule:
        The person who reaches 21 will lose the game
constraints:
         Every time enter a single value 
         Enter the valid inputs 
"""
try:
 print("lets play 21 game")
 numbers=[0]
 while True:
    user_ch=int(input("Enter any number 1,2 or 3:"))
    while user_ch not in [1,2,3]:
        print("Invalid input ! Re-Enter")
        user_ch = int(input("Enter any number 1,2 or 3:"))
    for i in  range(user_ch):
        value=int(input("Enter your value:"))
        while value in numbers:
            print("Value is already present in list!Re-enter")
            value = int(input("Enter your value:"))
        if value<numbers[-1]:
            print("Enter the value bigger than previous")
            print("You loss a chance")
            continue
        numbers.append(value)
    print("After you entered values are:")
    print(numbers)
    if numbers[-1]>=20:
        print("You loss the game")
        print("Computer win")
        break
    computer_ch=4-user_ch
    for i in range(computer_ch):
        numbers.append(numbers[-1]+i+1)
    print("After computer entered values are:")
    print(numbers)
    if numbers[-1]>=20:
        print("You won the game")
        break
except Exception:
    print("Invalid input! Re-run the program")