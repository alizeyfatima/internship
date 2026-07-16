import random
choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
ties = 0

while True:
    player = input("Choose rock, paper, scissors (or quit): ").lower()

    if player == "quit":
        print("Game ended!")
        break

    if player not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
        ties +=1
    elif (player == "rock" and computer == "scissors"):
        print("You win!")
        player_score +=1
    elif (player == "paper" and computer == "rock"):
        print("You win!")
        player_score +=1  
    elif (player == "scissors" and computer == "paper"):
        print("You win!")
        player_score +=1
    else:
        print("Computer wins!")
        computer_score +=1

print("Final Scores:")
print("Player:", player_score)
print("Computer:", computer_score)
print("Ties:", ties)