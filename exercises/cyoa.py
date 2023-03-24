"""My attempt to be creative with my schoolwork."""

__author__ = "730481986"


import random
points: int = 0
player: str = ""
player_hp: int = 10
opponent_hp: int = 10

def main() -> None:
    """Main function of the game."""
    global points
    greet()
    global player_hp
    global opponent_hp
    FIRST_EMOJI: str = "\U0001F947"
    SECOND_EMOJI: str = "\U0001F948"
    while player_hp > 0 and opponent_hp > 0:
        player_attack(int(input(f"{player} chose your punch; 1 for jab, 2 for hook, and 3 for uppercut.  Press 4 to end the game: ")))
        print(f"Points for {player}: {points}, Health for {player}: {player_hp}, Opponent's health: {opponent_hp}.")
        print("Now it is the opponents turn")
        opponent_attack()
        print(f"Points for {player}: {points}, Health for {player}: {player_hp}, Opponent's health: {opponent_hp}.")
    if player_hp > 0:
        print(f"You win {player}!  Your score will now be entered into a point lottery; you can risk it all or walk away and lose nothing!")
        points = point_multiplier(points)
        print(f"Congradulations {player}, you won with {points} points! {FIRST_EMOJI}")
        return 
    if player_hp <= 0:
        print(f"Better luck next time {player}, you lost with {points} points :( {SECOND_EMOJI})")
        return
    

def greet() -> None:
    """Greets the player."""
    global player
    player = input("Welcome to One Round Knock-Out, the fast and furious punch out game!  Enter your name here: ")
    print(f"Welcome {player}!  The goal of this game is to knock out your opponent before they can do the same to you!  Each participant has 10 health, and can chose from a jab, hook, or uppercut.  Jabs land 75% of the time and do 1 damage, hooks 50% and 2 damage, and uppercuts 25% and 3 damage.")
    return


def player_attack(attack_type=int) -> int:
    """Tracks the player's attacks."""
    CLOWN_EMOJI: str = "\U0001F921"
    global opponent_hp
    global points
    if attack_type == 1:  # jab
        if random_number() > 1:
            points = points + 1
            opponent_hp = opponent_hp - 1
            return
        else:
            print(f"Miss!{CLOWN_EMOJI}")
            return
    if attack_type == 2:  # hook
        if random_number() > 2:
            points += 2
            opponent_hp = opponent_hp - 2
            return
        else:
            print(f"Miss!{CLOWN_EMOJI}")
            return
    if attack_type == 3:  # uppercut
        if random_number() > 3:
            points += 3
            opponent_hp -= 3
            return
        else:
            print(f"Miss!{CLOWN_EMOJI}")
            return
    if attack_type == 4:  #end game
        print(f"Play again soon!  {player} finished with {points} points and {player_hp} health.")
        quit()

def opponent_attack() -> None:
    """Tracks the opponent's attacks."""
    global points
    global player_hp
    opponent_point = random_number()
    taunt = int(input(f"(Opponent) - Be warned {player},  I will squish you like a bug!  (press 1 to taunt and receive +1 points, press 2 to say nothing and receive +1 health) "))
    if taunt == 1:
        print("+1 points")
        points += 1
    if taunt == 2:
        print("+1 health")
        player_hp += 1
    if opponent_point == 4:
        player_hp = player_hp - 3
        return
    if opponent_point == 3:
        player_hp = player_hp - 2
        return
    if opponent_point == 2:
        player_hp = player_hp - 1
        return
    if opponent_point == 1:
        return
    

def random_number() -> None:
    """Creates a random number between 1 and 4 to fight."""
    number: int = random.randint(1, 4)
    return number

def point_multiplier(x=int) -> int:
    """Optional point multiplier."""
    choice = int(input(f" {player}, select 1 for a chance to double your points!  50% chance you double and 50% you lose.  Select 2 to forgo the lottery and keep your points. "))
    if choice == 1:
        roll: int = random_number()
        if roll > 2:
            x *= 2
            print(f"Congradulations {player}!  You have doubled your point total!")
            return x
        if roll <= 2:
            x = 0
            print(f"Sorry {player}, you lost all your points :(")
            return x
    if choice == 2:
        return x


if __name__ == "__main__":
    main()
