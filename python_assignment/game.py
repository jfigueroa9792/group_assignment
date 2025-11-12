print("Welcome to Rock-Paper-Scissors!")
player_input = ''
while player_input not in ['rock','paper','scissors']:
    player_input = input("Choose rock, paper, or scissors: ").lower()
print(f"You chose: {player_input}")
