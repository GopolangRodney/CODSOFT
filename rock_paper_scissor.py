import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie!, Play Again"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "Computer Lose, You win!"
    else:
        return "You Lose, Computer wins!"


def play_round():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    
    while user_choice not in choices:
        print("Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    
    result = determine_winner(user_choice, computer_choice)
    print(result)

    return result


def play_game():
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        print("Round", rounds_played + 1)
        result = play_round()

        if "Computer Lose, You win!" in result:
            user_score += 1
        elif "You Lose, Computer wins!" in result:
            computer_score += 1
        
        rounds_played += 1
        print(f"Score: User {user_score} Vs {computer_score} Computer")

        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Final Score:")
    print(f"User: {user_score}, Computer: {computer_score}")
    print("Good Game Player!")


if __name__ == "__main__":
    print("Hey!, Lets Play!")
    play_game()
