def get_choices():
    options = ["rock", "paper", "scissors"]

    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()

    while player_choice not in options:
        print("Invalid choice!")
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    computer_chice = random.choice(options)

    return {"player": player_choice, "computer": computer_chice}

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return("It's a tie!")
    
    elif player == "rock":
        if computer == "scissors":
            return("Rock smashes scissors! You win!")
        else:
            return("Paper covers rock! You lose.")
    
    elif player == "paper":
        if computer == "rock":
            return("Paper covers rock! You win!")
        else:
            return("Scissors cuts paper! You lose.")
        
    elif player == "scissors":
        if computer == "paper":
            return("Scissors cuts paper! You win!")
        else:
            return("Rock smashes scissors! You lose.")

if __name__ == "__main__":
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
