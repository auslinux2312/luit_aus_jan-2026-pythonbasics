computer_select = "rock"
user_select = str(input("rock, paper, scissors? "))

if computer_select == user_select:
    print("It's a draw")
elif user_select == 'paper':
    print("You win!")
elif user_select == 'scissors':
    print('You lose! :(')
