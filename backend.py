import random
import time

# Function to set the difficulty level
def set_difficulty():
    while True:
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            return 10
        elif choice == '2':
            return 5
        elif choice == '3':
            return 3
        else:
            print("Invalid choice! Please select again.")

# Function to play a single round of the guessing game
def play_game():
    # Set up the game
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Random number selection
    number_to_guess = random.randint(1, 100)
    
    # Set difficulty
    chances = set_difficulty()
    print(f"\nYou have {chances} chances. Let's start the game!")
    
    # Start timer
    start_time = time.time()
    
    # Initialize variables
    attempts = 0
    user_won = False
    
    # Guessing loop
    while attempts < chances:
        try:
            guess = int(input(f"Enter your guess ({chances - attempts} chances left): ").strip())
            attempts += 1
            
            if guess == number_to_guess:
                user_won = True
                break
            elif guess > number_to_guess:
                print("Incorrect! The number is less than", guess)
            else:
                print("Incorrect! The number is greater than", guess)
        except ValueError:
            print("Please enter a valid number!")
    
    # End timer
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    
    # Check if user won or lost
    if user_won:
        print(f"\nCongratulations! You guessed the correct number in {attempts} attempts and {total_time} seconds.")
        return attempts, chances  # Return attempts and chances for high score tracking
    else:
        print(f"\nSorry, you've run out of chances! The correct number was {number_to_guess}.")
        return None, chances  # Return None if the user didn't win, along with chances

# Main function to start the game
def main():
    high_scores = {"Easy": None, "Medium": None, "Hard": None}
    
    while True:
        # Play a round
        attempts, chances = play_game()
        
        # Update high score
        if attempts is not None:
            if chances == 10:
                difficulty = "Easy"
            elif chances == 5:
                difficulty = "Medium"
            else:
                difficulty = "Hard"
            
            # Update the high score if this attempt is better
            if high_scores[difficulty] is None or attempts < high_scores[difficulty]:
                high_scores[difficulty] = attempts
                print(f"\nNew high score for {difficulty} difficulty: {attempts} attempts!")
        
        # Ask if the user wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThank you for playing! Here are the high scores:")
            for level, score in high_scores.items():
                if score is not None:
                    print(f"{level} difficulty: {score} attempts")
                else:
                    print(f"{level} difficulty: No high score yet.")
            break

if __name__ == "__main__":
    main()
