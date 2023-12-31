import random 
player1 = input("Select Rock, Paper, or Scissor :").lower()
player2 = random.choice(["Rock","Paper","scissor"]).lower()
print("Player 2 selected: ",player2)

if player1 == "Rock" and player2 == "Paper":
    print("Player 2 Won")
elif player1 == "Paper" and player2 == "Scissor":
    print("Player 2 Won")
elif player1 == "Scissor" and player2 == "Rock":
    print("Player 2 Won")
elif player1 == player2:
    print("It's a Tie")
else:
    print("Player 1 Won")