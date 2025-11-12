import random 


print("Welcome to Rock-Paper-Scissors!")
randNum = random.randint(1,3)

if(randNum == 1):
    print("Computer chose: rock")
if(randNum == 2):
    print("Computer chose: scissors")
if(randNum == 3):
    print("Computer chose: paper")
