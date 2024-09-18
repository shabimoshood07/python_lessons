# choices = ["rock", "paper", "scissors"]
#
# computer = random.choice(choices)
#
# player = input("rock, paper or scissors? ").lower()
#
# # while not choices.__contains__(player): #alternative method to check
# while player not in choices:
#     print("please make a valid choice")
#     player = input("rock, paper or scissors? ").lower()
#
# print(player)
# print(computer)


# choices = ["rock", "paper", "scissors"]
#
# computer = random.choice(choices)
#
# # Get player's choice and validate input
# while (player := input("rock, paper or scissors? ").lower()) not in choices:
#     print("Please make a valid choice.")
#
# print(f"Player: {player}")
# print(f"Computer: {computer}")


import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)

    # Get player's choice and validate input using the walrus operator
    while (player := input("rock, paper, or scissors? ").lower()) not in choices:
        print("Invalid choice, please try again.")

    # Show choices
    print(f"\nPlayer: {player}")
    print(f"Computer: {computer}")

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Play again ?
    if (play_again := input("\nDo you want to play again? (yes/no): ").lower()) != 'yes':
        print("Thanks for playing!!!")
        break

