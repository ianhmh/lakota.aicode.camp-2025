#!/usr/bin/env python3
"""
Hangman Game - Student Build Project
Day Two: Building a complete game from scratch

This script will be built by students during Sessions 2A and 2B.
It demonstrates functions, program organization, and turtle graphics.

Students: Build this step by step, testing each function as you go!
"""

import random
import turtle
import time

# ============================================================================
# CORE GAME FUNCTIONS (Session 2A)
# ============================================================================

def load_words(filename):
    """
    Load words from a text file and filter them for Hangman.
    
    Parameters:
        filename (str): Name of file containing words
    
    Returns:
        list: List of words suitable for Hangman (4-8 letters, letters only)
    """
    # TODO: Students implement this function
    # Hints:
    # - Use try/except for file handling
    # - Filter words: 4-8 letters, only alphabetic characters
    # - Convert to uppercase for consistency
    # - Provide backup words if file can't be loaded
    
    pass  # Remove this and add your code


def choose_word(word_list):
    """
    Choose a random word from the word list.
    
    Parameters:
        word_list (list): List of possible words
    
    Returns:
        str: A randomly chosen word
    """
    # TODO: Students implement this function
    # Hints:
    # - Use random.choice()
    # - Handle empty list case
    
    pass  # Remove this and add your code


def display_word_progress(word, guessed_letters):
    """
    Show the word with guessed letters revealed and unknown letters as blanks.
    
    Parameters:
        word (str): The secret word
        guessed_letters (list): Letters the player has guessed
    
    Returns:
        str: The word with blanks (e.g., "P _ _ H O N")
    """
    # TODO: Students implement this function
    # Hints:
    # - Loop through each letter in the word
    # - If letter was guessed, show it; otherwise show "_"
    # - Handle case sensitivity
    # - Return a nicely formatted string
    
    pass  # Remove this and add your code


def get_player_guess(guessed_letters):
    """
    Get a valid letter guess from the player.
    
    Parameters:
        guessed_letters (list): Letters already guessed
    
    Returns:
        str: A valid, new letter guess
    """
    # TODO: Students implement this function
    # Hints:
    # - Use input() to get user input
    # - Validate: single letter, not already guessed
    # - Convert to uppercase
    # - Keep asking until valid input
    
    pass  # Remove this and add your code


def check_guess(word, guess):
    """
    Check if a guessed letter is in the word.
    
    Parameters:
        word (str): The secret word
        guess (str): The guessed letter
    
    Returns:
        bool: True if guess is in word, False otherwise
    """
    # TODO: Students implement this function
    # Hints:
    # - Use 'in' operator
    # - Handle case sensitivity
    
    pass  # Remove this and add your code


def is_word_complete(word, guessed_letters):
    """
    Check if all letters in the word have been guessed.
    
    Parameters:
        word (str): The secret word
        guessed_letters (list): Letters the player has guessed
    
    Returns:
        bool: True if word is complete, False otherwise
    """
    # TODO: Students implement this function
    # Hints:
    # - Check if every letter in word is in guessed_letters
    # - Handle case sensitivity
    # - Return True only if ALL letters are guessed
    
    pass  # Remove this and add your code


# ============================================================================
# GRAPHICS FUNCTIONS (Session 2B)
# ============================================================================

def setup_graphics():
    """
    Set up the turtle graphics window and create drawing turtle.
    
    Returns:
        tuple: (screen, drawing_turtle) for the game
    """
    # TODO: Students implement this function in Session 2B
    # Hints:
    # - Create screen with appropriate size
    # - Set background color
    # - Create turtle for drawing
    # - Set turtle properties (speed, color, etc.)
    
    pass  # Remove this and add your code


def draw_gallows():
    """
    Draw the gallows (the wooden structure for hanging).
    This is drawn once at the start of each game.
    """
    # TODO: Students implement this function in Session 2B
    # Hints:
    # - Draw a simple gallows structure
    # - Base, vertical post, horizontal beam, noose
    # - Position appropriately on screen
    
    pass  # Remove this and add your code


def draw_hangman_part(wrong_count):
    """
    Draw one part of the hangman figure based on wrong guess count.
    
    Parameters:
        wrong_count (int): Number of wrong guesses (1-6)
    """
    # TODO: Students implement this function in Session 2B
    # Hints:
    # - wrong_count 1: head
    # - wrong_count 2: body  
    # - wrong_count 3: left arm
    # - wrong_count 4: right arm
    # - wrong_count 5: left leg
    # - wrong_count 6: right leg (game over)
    
    pass  # Remove this and add your code


def display_game_info(word, guessed_letters, wrong_count, max_wrong):
    """
    Display current game information on the graphics screen.
    
    Parameters:
        word (str): The secret word
        guessed_letters (list): Letters guessed so far
        wrong_count (int): Number of wrong guesses
        max_wrong (int): Maximum wrong guesses allowed
    """
    # TODO: Students implement this function in Session 2B
    # Hints:
    # - Show word progress with blanks
    # - Show guessed letters
    # - Show wrong guess count
    # - Position text nicely on screen
    
    pass  # Remove this and add your code


def show_game_result(won, word):
    """
    Display the final game result (won or lost).
    
    Parameters:
        won (bool): True if player won, False if lost
        word (str): The secret word
    """
    # TODO: Students implement this function in Session 2B
    # Hints:
    # - Show "You Won!" or "You Lost!" message
    # - Reveal the word
    # - Make it visually appealing
    
    pass  # Remove this and add your code


# ============================================================================
# MAIN GAME LOGIC
# ============================================================================

def play_hangman():
    """
    Play one complete game of Hangman.
    
    Returns:
        bool: True if player wants to play again, False otherwise
    """
    print("🎮 Starting new Hangman game!")
    
    # Game setup
    words = load_words("1-1000.txt")
    if not words:
        print("No words available! Using default word.")
        secret_word = "PYTHON"
    else:
        secret_word = choose_word(words)
    
    # Game state
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6
    
    print(f"I'm thinking of a {len(secret_word)}-letter word...")
    print("Guess one letter at a time. You get 6 wrong guesses!\n")
    
    # Main game loop
    while True:
        # Show current state
        progress = display_word_progress(secret_word, guessed_letters)
        print(f"Word: {progress}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print()
        
        # Check win condition
        if is_word_complete(secret_word, guessed_letters):
            print(f"🎉 Congratulations! You guessed '{secret_word}'!")
            return True
        
        # Check lose condition
        if wrong_guesses >= max_wrong:
            print(f"💀 Game Over! The word was '{secret_word}'.")
            return False
        
        # Get player's guess
        guess = get_player_guess(guessed_letters)
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if check_guess(secret_word, guess):
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"❌ Sorry, '{guess}' is not in the word.\n")


def main():
    """
    Main function to run the Hangman game.
    Handles multiple games and user interface.
    """
    print("🎯 WELCOME TO HANGMAN!")
    print("=" * 25)
    print("Guess the word one letter at a time.")
    print("You lose if the hangman drawing is completed!")
    print()
    
    games_played = 0
    games_won = 0
    
    # Game loop
    while True:
        games_played += 1
        won = play_hangman()
        
        if won:
            games_won += 1
        
        # Show statistics
        print(f"\nGame Statistics:")
        print(f"Games played: {games_played}")
        print(f"Games won: {games_won}")
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f"Win rate: {win_rate:.1f}%")
        
        # Ask to play again
        while True:
            play_again = input("\nPlay again? (y/n): ").lower().strip()
            if play_again in ['y', 'yes']:
                print("\n" + "="*50 + "\n")
                break
            elif play_again in ['n', 'no']:
                print("\nThanks for playing Hangman! Goodbye! 👋")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")


# ============================================================================
# TESTING FUNCTIONS (Remove after testing)
# ============================================================================

def test_functions():
    """
    Test individual functions. Students can run this to check their work.
    """
    print("🧪 TESTING HANGMAN FUNCTIONS")
    print("=" * 30)
    
    # Test word loading
    print("Testing load_words()...")
    words = load_words("1-1000.txt")
    if words:
        print(f"✅ Loaded {len(words)} words")
        print(f"Sample words: {words[:5]}")
    else:
        print("❌ No words loaded")
    print()
    
    # Test word selection
    print("Testing choose_word()...")
    test_words = ['PYTHON', 'TURTLE', 'CODING']
    for i in range(3):
        word = choose_word(test_words)
        print(f"Random word {i+1}: {word}")
    print()
    
    # Test guess checking
    print("Testing check_guess()...")
    test_word = "PYTHON"
    test_letters = ['P', 'X', 'Y', 'Z']
    for letter in test_letters:
        result = check_guess(test_word, letter)
        status = "✅" if result else "❌"
        print(f"'{letter}' in '{test_word}': {status}")
    print()
    
    # Test word progress
    print("Testing display_word_progress()...")
    guesses = ['P', 'Y', 'X']
    progress = display_word_progress(test_word, guesses)
    print(f"Word: {test_word}")
    print(f"Guesses: {guesses}")
    print(f"Progress: {progress}")
    print()
    
    # Test completion check
    print("Testing is_word_complete()...")
    complete_guesses = ['P', 'Y', 'T', 'H', 'O', 'N']
    is_complete = is_word_complete(test_word, complete_guesses)
    print(f"All letters guessed: {is_complete}")


# ============================================================================
# SCRIPT EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Students: Uncomment the line below to test your functions
    # test_functions()
    
    # Students: Uncomment the line below to run the full game
    # main()
    
    print("🚀 Hangman Game Template Ready!")
    print()
    print("📝 TO GET STARTED:")
    print("1. Implement the functions marked with 'TODO'")
    print("2. Test each function using test_functions()")
    print("3. Run the full game using main()")
    print("4. Add graphics in Session 2B!")
    print()
    print("💡 Remember: Build one function at a time and test as you go!")
    print("Good luck building your game! 🎮")