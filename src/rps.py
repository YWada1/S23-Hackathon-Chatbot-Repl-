import random

class Rps:
  def playrps(self):
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    if user_action != possible_actions:
        "that's not a choice"
    print(f"\nYou chose {user_action}, Regina chose {computer_action}.\n")

    if user_action == computer_action:
      print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
      if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
      else:
        print("Paper covers rock! You lose.\n")
    elif user_action == "paper":
      if computer_action == "rock":
        print("Paper covers rock! You win!\n")
      else:
        print("Scissors cuts paper! You lose.\n")
    elif user_action == "scissors":
      if computer_action == "paper":
        print("Scissors cuts paper! You win!\n")
      else:
        print("Rock smashes scissors! You lose.\n")
    else:
        print("Please use one of the commands!")
        return