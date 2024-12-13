import random

options = ["rock", "paper", "scissors"]
user_win = 0
computer_win = 0

def randomer():
    return random.choice(options)

while True:
    roll = input("Type rock/paper/scissors to play or q to quit: ").lower()
    if roll == "q":
        break

    if roll not in options:
        print("Invalid choice, try again.")
        continue

    computer_pick = randomer()
    print(f"Computer picked {computer_pick}")

    if (roll == "rock" and computer_pick == "scissors") or \
       (roll == "paper" and computer_pick == "rock") or \
       (roll == "scissors" and computer_pick == "paper"):
        print("You won")
        user_win += 1
    elif roll == computer_pick:
        print("It's a tie")
    else:
        print("You lose")
        computer_win += 1

print(f"You won {user_win} times")
print(f"The computer won {computer_win} times")
