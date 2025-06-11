import random
while True:
    player = input("================================\nRock Paper Scissors Lizard Spock\n================================\n\n1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖\n6) For Rules\n7) Exit\nPick a number: ")
    computer = random.randint(1, 5)
    if player == "1":
        player = "✊"
    elif player == "2":
        player = "✋"
    elif player == "3":
        player = "✌️"
    elif player == "4":
        player = "🦎"
    elif player == "5":
        player = "🖖"

    if computer == 1:
        computer = "✊"
    elif computer == 2:
        computer = "✋"
    elif computer == 3:
        computer = "✌️"
    elif computer == 4:
        computer = "🦎"
    elif computer == 5:
        computer = "🖖"

    if player == "✊" and computer == "✋":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "✊" and computer == "✌️":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "✊" and computer == "🦎":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "✊" and computer == "🖖":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "✋" and computer == "✊":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "✋" and computer == "✌️":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "✋" and computer == "🦎":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "✋" and computer == "🖖":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "✌️" and computer == "✊":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "✌️" and computer == "✋":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "✌️" and computer == "🦎":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "✌️" and computer == "🖖":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "🦎" and computer == "✊":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "🦎" and computer == "✋":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "🦎" and computer == "✌️":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "🦎" and computer == "🖖":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "🖖" and computer == "✊":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "🖖" and computer == "✋":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == "🖖" and computer == "✌️":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe player won!")
    elif player == "🖖" and computer == "🦎":
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nThe CPU won!")
    elif player == computer:
        print(f"\nYou chose: {player}\nCPU chose: {computer}\nIt's a tie!")
    elif player == "6":
        print("""\nScissors cut Paper.
                \nPaper covers Rock.
                \nRock crushes Lizard.
                \nLizard poisons Spock.
                \nSpock smashes Scissors.
                \nScissors beat Lizard.
                \nLizard eats Paper.
                \nPaper disproves Spock.
                \nSpock vaporizes Rock.
                \nRock breaks Scissors.""")
    elif player == "7":
        print("\nExiting the game. Goodbye!")
        break
    else:
        print("\nInvalid input! Please choose a number between 1 and 6.")
