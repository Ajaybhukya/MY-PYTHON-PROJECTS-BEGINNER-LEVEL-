questions = (
    ("What is the capital of France?"),
    ("Which planet is known as the Red Planet?"),
    ("Who wrote the famous novel 'To Kill a Mockingbird'?"),
    ("What is the largest mammal on Earth?"),
    ("Which music group's original members were John, Paul, George, and Ringo?")
)
options=(
    ('A.India','B.Paris','C.China','D.Nepal'),
        ('A.Mars','B.Earth','C.Venus','D.Jupiter'),
        ('A.Ernest Hemingway','B.F. Scott Fitzgerald','C.Harper Lee','D.George Orwell'),
        ('A.Blue whale','B.Giant squid','C.Hippopotamus','D.Crickets')  ,
        ('A.The Who','B.The Rolling Stones','C.The Doors','D.The Beatles')
         )
correct_answers=('B','A','C','A','D')
question_number=0
guess_option=[]
score=0
for question in questions:
    print('-------------------------')
    print(question)
    for option in options[question_number]:
        print(option)
    guess=input("Enter a Option(A,B,C,D):").upper()
    guess_option.append(guess)
    if guess==correct_answers[question_number]:
        print("Correct Answer")
        score+=1
    else:
        print("Wrong Answer")
        print(f"correct answer is {correct_answers[question_number]}")
    question_number+=1
print('----------------')
print("----------Result------------")
print(f"Your score is {float(score)/len(correct_answers)*100}%")
print("Your guesses:",guess_option)
print("Original Answers:",correct_answers)