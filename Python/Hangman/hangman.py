import random


def main():
    won = 0
    loss = 0
    while True:
        lives = 6  # Total no.of lives.

        # Ask if the user wants to play or not.
        play = input("Do you want to play the game (press 'y' for yes and 'q' for quit): ").lower()
        if play == 'q':
            score(won,loss)
            break
        elif play != 'y':
            print("Invalid Input!")
            continue

        # Ask user what difficulty do they want to play in
        while True:
            difficulty = input("Enter the difficulty(easy, medium, hard): ").lower()
            if difficulty in ('easy', 'medium', 'hard'):
                break
            else:
                print("Invalid Input!")
                continue

        word = random.choice(words(difficulty))  # Randomly pick a word based on difficulty
        guessed = set()  # Store guessed letters

        while lives > 0:
            print(f"lives = {lives}")

            # Show the words with guessed letters revealed
            display = [c if c in guessed else '_' for c in word]
            print("Word: " + " ".join(display))
            print(f"Lives left: {lives}")

            # If no '_' left user has won
            if '_' not in display:
                print("🎉 You guessed it!")
                won += 1 # Track Wins
                break

            # dashes for each letter
            for i in range(len(word)):
                print(" _ ", end="")
            print()

            # Ask user for their guess
            while True:
                guess = input("Enter a letter: ").lower()
                if len(guess) == 1 and guess.isalpha():
                    break
                else:
                    print("Invalid Input!")
                    continue

            # Check if they have already guessed the letter or not.
            if guess in guessed:
                print("You have already guessed this letter")
            else:
                # Check if guessed letter is correct
                if not check(guess, word,):
                    print("Incorrect")
                    lives -= 1
                    hangman(6 - lives)

                    # Ask if the user want's a hint
                    want_hint = input("Do you want a hint? (press 'y' for yes and 'n' for no): ").lower()
                    if want_hint == 'y':
                        hint(word, guessed)

                else:
                    print("Correct")
                    guessed.add(guess)

        else:
            print(f"💀 You lost! The word was: {word}")
            loss += 1 # Track losses


def words(difficulty):
    # List of words according to their difficulty
    easy = ['apple', 'chair', 'table', 'bread', 'plant',
            'house', 'smile', 'light', 'clock', 'green']
    medium = ['blanket', 'picture', 'battery', 'holiday', 'cabinet',
              'lantern', 'fiction', 'monitor', 'speaker', 'digital']
    hard = ['algorithm', 'microwave', 'knowledge', 'hemisphere', 'butterfly',
            'electricity', 'astronaut', 'telephone', 'adventure', 'challenge']

    # Return the list of words based on its difficulty
    if difficulty == 'easy':
        return easy
    elif difficulty == 'medium':
        return medium
    else:
        return hard


def check(guess, word):
    # Check if user's guess is correct or not
    return guess in word


def hangman(stage):
    # ASCII art stages for hangman drawing
    stages = [
        # 0 wrong guesses
        """
         +---+
         |   |
             |
             |
             |
        =======
        """,
        # 1 wrong guess
        """
         +---+
         |   |
         O   |
             |
             |
        =======
        """,
        # 2 wrong guesses
        """
         +---+
         |   |
         O   |
         |   |
             |
        =======
        """,
        # 3 wrong guesses
        """
         +---+
         |   |
         O   |
        /|   |
             |
        =======
        """,
        # 4 wrong guesses
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
        =======
        """,
        # 5 wrong guesses
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
        =======
        """,
        # 6 wrong guesses
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
        =======
        """
    ]
    # Show hangman for current stage.
    if stage < len(stages):
        print(stages[stage])


def hint(word, guessed):
    for c in word:
        if c not in guessed:
            print(f"💡 Hint: The word contains the letter '{c}'")
            return


def score(won, loss):
    print(f"\n🏁 Final Score")
    print(f"Wins: {won}")
    print(f"Losses: {loss}")
    print(f"Total Score: {max(won - loss, 0)}")



# Start the game.
if __name__ == "__main__":
    main()
