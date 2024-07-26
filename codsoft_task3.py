import random

print('''Winning rules of the game ROCK PAPER SCISSORS are :\nRock vs Paper -> Paper wins \nRock vs Scissors -> Rock wins\nPaper vs Scissors -> Scissor wins \n''')

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    ch = int(input("Enter your choice :"))

    while ch > 3 or ch < 1:
        choice = int(input('Enter a valid choice please '))

    if ch == 1:
        choice = 'Rock'
    elif ch == 2:
        choice = 'Paper'
    else:
        choice = 'Scissors'

    print('Your choice is', choice)
    choices=["Rock","Paper",'Scissors']
    comp_choice = random.choice(choices)

    print("Computer choice is", comp_choice)
  
    if choice == comp_choice:
        print('Its a Draw')
 
    elif choice=='Paper' and comp_choice == 'Rock':
        print("You Win")
    
    elif choice=='Scissors' and comp_choice == 'Paper':
        print("You Win")
    
    elif choice=='Rock' and comp_choice == 'Scissors':
        print("You Win")

    elif comp_choice=='Paper' and choice == 'Rock':
        print("Computer Win")
    
    elif comp_choice=='Scissors' and choice == 'Paper':
        print("Computer Win")
    
    elif comp_choice=='Rock' and choice == 'Scissors':
        print("Computer Win")

    print("Do you want to play again? (Y/N)")

    ans = input().lower()
    if ans == 'n':
        break

print("thanks for playing")

