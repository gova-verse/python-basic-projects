#guessing_game,py
#concepts: while loop, if/elif/else, random module, functions, counters
import random
def get_random_number(min_val, max_val):
    #random. randint returns a random whole number between min and max(inclusive)
    return random. randint(min_val,max_val)
def check_guess(guess, secret):
    #compare guess to secret number and return a hint
    if guess < secret:
        return"too low"
    elif guess> secret:
        return"too high"
    else:
        return "correct"
def play_game():
    print("="* 35)
    print("     Number guessing Game")
    print("="* 35)

    min_val = 1
    max_val = 100
    secret_number = get_random_number(min_val, max_val)
    attempts = 0
    max_attempts = 7

    print(f"\nI picked a number between {min_val} and {max_val}.")
    print(f"You have {max_attempts} attempts. Good luck\n")

    while attempts < max_attempts:
        #attempts left
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")

        #get user guess and validate it
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number:\n")
            continue
        #checck if guess is in valid range
        if guess < min_val or guess > max_val:
            print(f"Please guess between {min_val} and {max_val}!\n")
            continue
        attempts += 1
        result = check_guess(guess, secret_number)

        if result =="correct":
            print(f"\nCorrect! You guessed it in {attempts} attempt(s)!")
            if attempts ==1:
                print("Incredible! First try!")
            elif attempts == 1:
                print("Amazing That was fast!")
            else:
                print("Well done!")
            return True
        else:
            print(f"Your guess is {result}:\n")

    # loop ended without correct guess
    print(f"\nGame over! You ran out of attempts.")
    print(f"The secret number was: {secret_number}")
    return False
def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again !="yes":
            print("\nThanks for playing. Have a nice day! ")
            break
if __name__ == "__main__":
   main()