"""My attempt to be creative with my schoolwork."""

__author__ = "730481986"


def main() -> None:
    global points
    points = 0
    greet()
    player_health()
    opponent_health()
    FIRST_EMOJI: str = "\U0001F947"
    SECOND_EMOJI: str = "\U0001F948"
    while player_hp or opponent_hp > 0:
        player_attack(input(f"{player} chose your punch; 1 for jab, 2 for hook, and 3 for uppercut"))
        print(f"Points for {player}: {points}, Health for {player}: {player_hp}, Opponent's health: {opponent_hp}.")
        print("Now it is the opponents turn")
        opponent_attack()
        print(f"Points for {player}: {points}, Health for {player}: {player_hp}, Opponent's health: {opponent_hp}.")
    if player_hp > 0:
        return f"Congradulations {player}, you won with {points} points! {FIRST_EMOJI}"
    if player_hp == 0:
        return f"Better luck next time {player}, you lost with {points} points :( {SECOND_EMOJI})"


def greet() -> None:
    """Greets the player."""
    global player
    player: str = input("Welcome to One Round Knock-Out, the fast and furious punch out game!  Enter your name here: ")
    print(f"Welcome {player}!  The goal of this game is to knock out your opponent before they can do the same to you!  Each participant has 10 health, and can chose from a jab, hook, or uppercut.  Jabs land 75% of the time and do 1 damage, hooks 50% and 2 damage, and uppercuts 25% and 3 damage.")
    return player


def player_attack(attack_type = int) -> int:
    """Tracks the player's attacks."""
    CLOWN_EMOJI: str = "\U0001F921"
    if attack_type == 1: #this is the jab
        if random_number() > 1:
            points += 1
            opponent_hp = opponent_hp - 1
            return "Tis only a scratch"
        else:
            return f"Miss!{CLOWN_EMOJI}"
    if attack_type == 2: #this is the hook
        if random_number() > 2:
            points += 2
            opponent_hp = opponent_hp - 2
            return "OOF!"
        else:
            return f"Miss!{CLOWN_EMOJI}"
    if attack_type == 3: #this is the uppercut
        if random_number() > 3:
            points += 3
            opponent_hp -= 3
            return "That's gotta hurt!"
        else:
            return f"Miss!{CLOWN_EMOJI}"


def player_health() -> None:
    """Tracks a player's health."""
    global player_hp
    player_hp = 10

    
def opponent_attack(difficulty = int) -> int:
    """Tracks the opponent's attacks."""
    opponent_point = random_number
    if opponent_point == 4:
        player_hp -= 3
        return "That's gotta hurt!"
    if opponent_point == 3:
        player_hp -= 2
        return "OOF!"
    if opponent_point == 2:
        player_hp -= 1
        return "Tis only a scratch"
    if opponent_point == 1:
        return "They missed you!"
    

def opponent_health() -> int:
    """Tracks the opponent's health."""
    global opponent_hp
    opponent_hp = 10


def random_number() -> None:
    import random
    number: int = random.randint(1,4)
    return number

