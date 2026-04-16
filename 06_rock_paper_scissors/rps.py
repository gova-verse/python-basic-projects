# rps.py
# Concepts: functions, random module, loops, conditionals, score tracking

import random

CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock"     and computer == "scissors") or \
         (player == "paper"    and computer == "rock")     or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def show_scores(scores):
    print("\n--- Current Scores ---")
    print(f"  You      : {scores['player']}")
    print(f"  Computer : {scores['computer']}")
    print(f"  Draws    : {scores['draws']}")

def show_menu():
    print("\n" + "=" * 40)
    print("       Rock Paper Scissors")
    print("=" * 40)
    print("  Enter 'rock', 'paper', or 'scissors'")
    print("  Enter 'score' to see scores")
    print("  Enter 'quit' to exit")
    print("=" * 40)

def play_round(scores):
    show_menu()
    player_choice = input("\nYour choice: ").lower().strip()

    if player_choice == "quit":
        return False
    elif player_choice == "score":
        show_scores(scores)
        return True
    elif player_choice not in CHOICES:
        print("Invalid choice! Enter rock, paper, or scissors.")
        return True

    computer_choice = get_computer_choice()
    print(f"\n  You chose    : {player_choice}")
    print(f"  Computer chose: {computer_choice}")

    result = get_winner(player_choice, computer_choice)

    if result == "player":
        print("  Result: You WIN this round!")
        scores["player"] += 1
    elif result == "computer":
        print("  Result: Computer WINS this round!")
        scores["computer"] += 1
    else:
        print("  Result: It's a DRAW!")
        scores["draws"] += 1

    return True

def main():
    print("=" * 40)
    print("   Welcome to Rock Paper Scissors!")
    print("=" * 40)

    scores = {"player": 0, "computer": 0, "draws": 0}
    rounds = 0

    while True:
        keep_playing = play_round(scores)
        if not keep_playing:
            rounds = scores["player"] + scores["computer"] + scores["draws"]
            print(f"\n--- Game Over! ---")
            print(f"  Total rounds played: {rounds}")
            show_scores(scores)
            if scores["player"] > scores["computer"]:
                print("\n  You are the overall WINNER!")
            elif scores["computer"] > scores["player"]:
                print("\n  Computer is the overall WINNER!")
            else:
                print("\n  Overall result is a DRAW!")
            break

if __name__ == "__main__":
    main()