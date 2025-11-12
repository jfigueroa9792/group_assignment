import random

print("Welcome to Rock-Paper-Scissors!")

numberPicked = random.randint(1,3)

if numberPicked == 1:
    print("Computer chose: rock")
if numberPicked == 2:
    print("Computer chose: scissors")
if numberPicked == 3:
    print("Computer chose: paper")