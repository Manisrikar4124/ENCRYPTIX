import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Initialize scores
user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
print("Enter 'quit' to end the game.")

while True:
    print("\nCurrent Score - You:", user_score, "Computer:", computer_score)
    
    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice == 'quit':
        print("Thanks for playing!")
        break
    
    # Computer random choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Determine winner
    result = determine_winner(user_choice, computer_choice)
    
    # Display choices and result
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)
    
    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    
    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
