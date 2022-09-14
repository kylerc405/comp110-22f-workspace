"""EX02 - One-Shot Wordle."""

__author__ = "730564343"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji: str = ""

word = "python"
guess: str = input(f"What is your {len(word)}-letter guess? ")

# Checking for correct length
while len(guess) != len(word):
    guess = input(f"That was not {len(word)} letters! Try again: ")


while index < len(word): 
    altmatch: int = 0
    exists: bool = False

    # Prints green box if the letter of the guess and the letter of the secret word match
    if guess[index] == word[index]:
        emoji += GREEN_BOX
    else:
        # Searches for any other occurrences of the guessed letter
        while exists is False and altmatch < len(word):
            if guess[index] == word[altmatch]:
                exists = True
            else:
                altmatch += 1
        # adds a yellow box if the guess letter is found at any other position, and a white box if not
        if exists is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX       

    index = index + 1
# prints the final output emoji
print(emoji)

# prints final output and exits program 
if guess == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")