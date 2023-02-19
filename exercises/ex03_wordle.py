"""EX03 - Wordle - This time it's the real deal"""

__author__ = "730481986"
def contains_char(whole_string = str, single_string = str) -> bool:
    """Determines whether or not a character is found in a string"""
    assert len(single_string) == 1
    chr_idx : int = 0
    while chr_idx <= (len(whole_string) - 1):
        if (single_string == whole_string[chr_idx]):
            return True
        else:
            chr_idx = chr_idx + 1
            if chr_idx == (len(whole_string)):
                return False

def emojified(guess = str, secret = str) -> str:
    """Returns the wordle emojis that indicate where certain letters are in the secret word"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    chr_idx : int = 0
    emoji_string: str = ""
    while chr_idx < len(guess):
        if (guess[chr_idx] == secret[chr_idx]):
            emoji_string = emoji_string + GREEN_BOX
        else:
            if contains_char(secret,guess[chr_idx]) == False:
                emoji_string = emoji_string + WHITE_BOX
            else:
                emoji_string = emoji_string + YELLOW_BOX
        chr_idx = chr_idx + 1
    return emoji_string

def input_guess(word_length = int) -> str:
    """Makes sure that the input matches the correct word length specified"""
    guess: str = input(f"Enter a {word_length} character word: ")
    while len(guess) != word_length:
        guess: str = input(f"That wasn't {word_length} chars! Try again: ")
    if len(guess) == word_length:
        return guess

def main() -> None:
    """The entry point of the program and main game loop."""
    user_turns: int = 1
    SECRET_WORD: str = "codes"
    while user_turns <= 6:
        print(f"=== Turn {user_turns}/6 ===")
        guess: str = input_guess(len(SECRET_WORD))
        print(emojified(guess, SECRET_WORD))
        if guess == SECRET_WORD:
            return print(f"You won in {user_turns}/6 turns!")
        else:
            user_turns = user_turns + 1
    return print("X/6 - Sorry, try again tomorrow!")