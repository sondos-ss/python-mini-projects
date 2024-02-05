import random

def choose_word():
    words = ["elephant", "computer", "sunshine", "chocolate", "adventure", "symphony", "butterfly", "kangaroo", "blueprint", "carousel", "puzzle", "fireworks", "galaxy", "whirlwind", "jazz", "raspberry", "enigma", "lighthouse", "avalanche", "umbrella"]
    return random.choice(words)

def display_word(word,letters):
    display=""
    for letter in word:
        if letter in letters:
            display+=letter
        else:
            display += "_"
    return display

def hangman():
    word=choose_word()
    letters=[]
    attempts_left = 6

    print("Welcome to Hangman!")

    while attempts_left>0:
        current_display = display_word(word,letters)
        print(f"Word: {current_display}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter: ").lower()

        if guess in letters:
            print("You already guessed that letter. Try again.")
            continue

        letters.append(guess)

        if guess not in word:
            attempts_left -= 1
            print("Incorrect guess!")
        else:
            print("Correct guess!")

        if all(letter in letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break

    if attempts_left == 0:
        print(f"Sorry, you ran out of attempts. The correct word was: {word}")

if __name__ == "__main__":
    hangman()