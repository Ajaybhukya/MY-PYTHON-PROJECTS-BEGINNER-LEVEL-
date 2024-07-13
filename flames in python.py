
def flames(name1,name2):
    name1=name1.replace(" ","").lower()
    name2=name2.replace(" ","").lower()
    unique_letters=set(name1+name2)
    common_letters=sum(1 for letters in unique_letters if letters in name1 and letters in name2)
    categories=['Friends','Love','Attraction','Marriage','Enemy','sister']
    result_index=(len(unique_letters)-common_letters)%len(categories)
    return categories[result_index]
try:
    player1=input("Enter your name:")
    player2=input("Enter your crush name:")
    if player1=='' or player2=='':
        print("Enter atleat a single letter")
        exit(0)
    if any(c.isdigit() for c in player1+player2):
        print("You entered number")
        print("So FLAMES not possible")
        exit(0)
    result=flames(player1,player2)
    print(f"According to FLAMES\nRelationship:{result}")
except Exception:
    print("Invalid input!")