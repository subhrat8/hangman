import random

def play_hangman():
    words_with_hints = [
        ("apple", "A red or green fruit"),
        ("banana", "A long yellow fruit"),
        ("grape", "A small purple or green fruit"),
        ("orange", "A round citrus fruit"),
        ("melon", "A large fruit with a thick rind")
    ]

    word, hint = random.choice(words_with_hints)
    guessed_letters = []
    attempts = 6

    print("\nWelcome to Hangman!")
    print("Hint:", hint)
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter or word: ").lower()

        # Already guessed check
        if guess in guessed_letters:
            print("You already guessed that.")
            continue

        # If user guesses the full word correctly
        if guess == word:
            print("🎉 You guessed the whole word correctly:", word)
            break

        # If it's a multi-letter guess (like "aple")
        elif len(guess) > 1:
            correct_any = False
            for ch in guess:
                if ch in word and ch not in guessed_letters:
                    guessed_letters.append(ch)
                    correct_any = True
            if not correct_any:
                attempts -= 1
                print(f"❌ None of those letters are correct! Attempts left: {attempts}")
            else:
                print("✔ Some letters were correct and filled in.")

        # If it's a single letter
        elif len(guess) == 1:
            guessed_letters.append(guess)
            if guess in word:
                print("Good guess!")
            else:
                attempts -= 1
                print(f"Wrong guess! Attempts left: {attempts}")

        # Show word progress
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print(display.strip())

        # Win condition
        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("💀 Game Over! The word was:", word)

# Main loop
while True:
    play_hangman()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break