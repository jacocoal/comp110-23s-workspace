"""EX01 - One Shot Wordle - Just like Eminem... you only get one shot"""

__author__ = "730481986"
SECRET: str = "python"
secret_var: int = len(SECRET)
guess: str = input(f"What is your {secret_var}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx_var: int = 0
chr_emoji: str = ""
found_elsewhere: bool = False
alt_idx: int = 0
while (len(guess) != secret_var):
    guess = input(f"That was not {secret_var} letters! Try again: ")
if (len(guess) == secret_var):
    while idx_var < secret_var:
        if (SECRET[idx_var] == guess[idx_var]):
            chr_emoji = chr_emoji + GREEN_BOX + ""
        if (SECRET[idx_var] != guess[idx_var]):
            while not(found_elsewhere == True) and alt_idx < idx_var:
                if (guess[idx_var] == SECRET[alt_idx]):
                    found_elsewhere = True 
                if (guess[idx_var] != SECRET[alt_idx]):
                    alt_idx = alt_idx + 1
            if (found_elsewhere == True):
                chr_emoji = chr_emoji + YELLOW_BOX + ""
            if (found_elsewhere != True):
                chr_emoji = chr_emoji + WHITE_BOX + ""
            found_elsewhere = False 
        idx_var = idx_var + 1
    if (SECRET != guess):
            print("Not quite. Play again soon!")
            print(chr_emoji)
            exit()
    else:
        if(SECRET == guess):
            print("Woo! You got it!")
            print(chr_emoji)
            exit()

    





