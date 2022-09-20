"""EX03 - Wordle."""
__author__ = "730564343"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, guess_char: str) -> bool:
    """contains_char searches for whether or not the secret word contains the character that has been guessed."""
    assert len(guess_char) == 1

    i = 0

    # Searches for any occurrences of the guessed letter
    while i < len(word):
        if guess_char == word[i]:
            return True
        else:
            i += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Produces emoji output of green, yellow, or white boxes."""
    assert len(guess) == len(secret)
    emoji: str = ""

    i = 0

    # Adds a green box if the letters match, a yellow box if the guessed letter is found elsewhere, and a white box if the letter is not found
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX

        elif contains_char(secret, guess[i]) is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX

        i += 1

    return emoji


def input_guess(length: int) -> str:
    """Obtains a guess from the player, and ensures the length matches the secret word."""
    word: str = input(f"enter a {length} character word: ")

    while len(word) != length:
        word = input(f"That wasn't {length} chars! Try again: ")
    
    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess: str = ""
    emoji_string: str = ""
    won: bool = False
    turn = 1

    correct: str = ""
    i = 0

    # Creates a string of all correct guess emojis 
    while i < len(secret_word):
        correct += GREEN_BOX
        i += 1
    # gives the user 6 turns to guess the correct word
    while won is False and turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret_word))
        print(guess)
        emoji_string = emojified(guess, secret_word)
        print(emoji_string)

        if emoji_string == correct:
            print(f"You won in {turn}/6 turns!")
            won = True
        elif emoji_string != correct:
            turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()