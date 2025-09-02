import random

def give_hint(secret_number):
    hints = []
    if secret_number % 2 == 0:
        hints.append("The number is even.")
    else:
        hints.append("The number is odd.")
    
    if secret_number % 3 == 0:
        hints.append("The number is divisible by 3.")
    if secret_number % 5 == 0:
        hints.append("The number is divisible by 5.")
    
    # Pick one random hint
    return random.choice(hints)

def number_guessing_game():
    print("🎯 Welcome to the Advanced Number Guessing Game!")
    
    while True:
        # Optional: Let user choose range
        lower = 1
        upper = 100
        secret_number = random.randint(lower, upper)
        max_attempts = 10
        attempts = 0
        used_hint = False

        print(f"\nI have selected a number between {lower} and {upper}.")
        print(f"You have {max_attempts} attempts to guess it.\n")

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("❌ Please enter a valid integer.\n")
                continue

            attempts += 1

            if guess < secret_number:
                print("⬆️ Too low!")
            elif guess > secret_number:
                print("⬇️ Too high!")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                score = max(0, (max_attempts - attempts + 1) * 10)
                print(f"🏆 Your score: {score}")
                break

            # Provide a hint after 3 wrong attempts, only once
            if attempts == 3 and not used_hint:
                hint = give_hint(secret_number)
                print(f"💡 Hint: {hint}")
                used_hint = True

            print(f"Attempts left: {max_attempts - attempts}\n")
        else:
            print(f"😔 Game over! The number was {secret_number}.")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("👋 Thanks for playing! Goodbye!")
            break

# Start the game
number_guessing_game()
