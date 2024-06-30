import random
def up_display(word,display,letter):
    new_display=''
    for i in  range(len(word)):
        if letter==word[i]:
            new_display+=letter
        else:
            new_display+=display[i]
    return new_display
def display_hangman(incorrect_attempts):
    stages=[
        """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
               """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]
    return stages[incorrect_attempts]
print("Lets play hangman game")
print(display_hangman(0))
word=random.choice(["mouse",'computer','python','c++'])
display="_"*len(word)
print("Intial display",display)
attempts=0
guessed_letters=[]
while True:
    guess=input("Enter a single letter:").lower()
    if guess in guessed_letters:
        print("You already gussed letter")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess")
        display=up_display(word,display,guess)
        print("After guess:",display)
        if '_' not in display:
            print("Congrajulations! you won the game")
            print("The world is:",word)
            break
    else:
        attempts+=1
        print("Incorrect guess")
        print(display_hangman(attempts))
        if attempts==6:
            print("You loss the game")
            print("The word is",word)
            break