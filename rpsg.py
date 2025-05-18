import random

# 1 for rock, 0 for paper, -1 for scissors
options = {"r": 1, "p": 0, "s": -1}
names = {1: "rock", 0: "paper", -1: "scissors"}

youchoice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()

if youchoice not in options:
    print("Invalid input! Please enter r, p, or s.")
else:
    you = options[youchoice]
    computer = random.choice([1, 0, -1])

    print(f"You chose {names[you]}")
    print(f"Computer chose {names[computer]}")

    if you == computer:
        print("It's a draw!")
    elif (you == 1 and computer == -1) or (you == 0 and computer == 1) or (you == -1 and computer == 0):
        print("You win!")
    else:
        print("You lose!")
