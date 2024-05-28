#Rock-Paper-Scissors Game
#User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
#Game Logic: Determine the winner based on the user's choice and the computer's choice. Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice. Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions and feedback.

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissor):")
        if user_choice in ["rock", "paper", "scissor"]:
            return user_choice
        else:
            print("Invalid choice! Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}\n")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'rock', 'paper', or 'scissors' to make your choice.")
    play_game()
