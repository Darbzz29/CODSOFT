def get_choice(player):
    choice = input("/n(player), enter Rock, Paper, Scissors: ").strip().lower()
    while choice not in ["Rock", "Paper", "Scissors"]:
        print("INvalid choice, please enter Rock, Paper, or Scissors")
        choice=input("/n{player}, enter Rock, Paper, or Scissors").strip().lower()
    return choice

def winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "its a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "scissors" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
def play_game():
    while True:
        print("/nWelcome!")
        player1_choice = get_choice("Player_1")
        player2_choice = get_choice("Player_2")
        print("/nResults:")
        print("/nPlayer 1 chose: {player1_choice.upper()}")
        print("/nPlayer 2 chose: {player2_choice.upper()}")
        print(winner(player1_choice, player2_choice))
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
        play_game()
