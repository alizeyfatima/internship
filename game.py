import random
choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
ties = 0
rounds = 0

while True:
    player = input("Choose rock, paper, scissors (or quit/end): ").lower()

    if player == "quit" or player == "end":
        print("Game over. Thanks for playing!")
        break

    if player not in choices:
        print("Invalid choice. Try again.")
        continue
    
    print("You chose:", player)

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
        ties +=1
    elif (player == "rock" and computer == "scissors"):
        print("You win! Rock smashes Scissors.")
        player_score +=1
    elif (player == "paper" and computer == "rock"):
        print("You win! Paper covers Rock.")
        player_score +=1  
    elif (player == "scissors" and computer == "paper"):
        print("You win! Scissors cuts Paper.")
        player_score +=1
    else:
        print("Computer wins! Better luck next time.")
        computer_score +=1
    rounds +=1

print("Final Scores:")
print("Player:", player_score)
print("Computer:", computer_score)
print("Ties:", ties)
print("Total Rounds played:", rounds)