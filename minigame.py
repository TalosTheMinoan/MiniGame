import random
import time

def get_difficulty():
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print("Invalid difficulty. Please choose easy, medium, or hard.")

def get_secret_number(difficulty):
    if difficulty == 'easy':
        return random.randint(1, 50)
    elif difficulty == 'medium':
        return random.randint(1, 100)
    else:
        return random.randint(1, 150)

def display_high_scores():
    try:
        with open("high_scores.txt", "r") as file:
            print("\nHigh Scores:")
            print(file.read())
    except FileNotFoundError:
        print("\nNo high scores available yet.")

def update_high_scores(score):
    try:
        with open("high_scores.txt", "a") as file:
            file.write(f"{score}\n")
    except FileNotFoundError:
        with open("high_scores.txt", "w") as file:
            file.write(f"{score}\n")

def play_guessing_game():
    print("Welcome to the Enhanced Guessing Game!")
    
    difficulty = get_difficulty()
    secret_number = get_secret_number(difficulty)
    attempts = 0
    max_attempts = 7
    score = 0

    print(f"I have selected a random number between 1 and {50 if difficulty == 'easy' else 100 if difficulty == 'medium' else 150}. Can you guess it?")

    start_time = time.time()

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)

                print(f"Congratulations! You guessed the correct number in {attempts + 1} attempts.")
                print(f"Time taken: {elapsed_time} seconds")
                
                # Adjust scoring based on attempts and time taken
                score += (max_attempts - attempts) * 10 - int(elapsed_time)

                update_high_scores(score)
                display_high_scores()
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"Attempts left: {remaining_attempts}")

            if attempts == 3:
                print(f"Hint: The number is {'even' if secret_number % 2 == 0 else 'odd'}.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

    print(f"Your score: {score}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_guessing_game()
    else:
        print("Thanks for playing!")

# Run the game
play_guessing_game()
