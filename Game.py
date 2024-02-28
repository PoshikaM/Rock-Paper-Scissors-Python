import random

print("Let's play Rock, Paper, Scissors!")

while True:
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break