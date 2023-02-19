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
