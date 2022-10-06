"""EX05 - Choose Your Own Adventure."""
__author__ = "730564343"

from random import randint

def main() -> None:
    global points, player, xp, level, zpoints, zdamage, ATTACK_EMOJI, HEALTH_EMOJI, BLOOD_EMOJI

    points= 100
    player = ""
    xp = 0
    level = 1
    zpoints = 20
    zpointsog = 20
    zdamage = 5

    ATTACK_EMOJI = "\U0001F5E1"
    HEALTH_EMOJI = "\U0001F9C9"
    BLOOD_EMOJI = "\U0001FA78"
    
    choice: str = ""

    greet()
    
    print(f"Alright, {player}. Get ready to fight some zombies. You can choose to Attack {ATTACK_EMOJI}, Heal {HEALTH_EMOJI}, or Quit the game. These first few levels are going to start off easy, so don't get too cocky. You're still bad.")
    
    while points > 0:
        print(f"Level {level}: zombie health = {zpoints}, zombie attack damage = {zdamage}.")
        
        while zpoints > 0:
            choice = input(f"Attack {ATTACK_EMOJI} (press 'a'), Heal {HEALTH_EMOJI} (press 'h'), or quit the game (press 'q')? ")

            if choice == "a":
                points = attack(points)
            elif choice == "h":
                heal()
            elif choice == "q":
                quit()
        
            if points <= 0:
                print(f"You died! Final level reached: {level}. That's embarrassing!")
                quit()
            
            if points == 101:
                zpoints = -1

        print("Congrats! Level complete!")
        print(f"{player} health restored to 100.")
        level += 1
        zpointsog += 5
        zpoints = zpointsog
        zdamage += 2
        points = 100



def greet() -> None:
    global player
    player = input("Hello! Welcome to Zombies. Your goal is to kill zombies. That's about it. What's your name? ")


def attack(health: int) -> int:
    global zpoints, zdamage, level, player

    print("Stab (25 damage, 50% chance of missing) or Slash (10 damage, 25% chance of missing)?")
    size: str = input("Press '1' for Stab, Press '2' for Slash: ")

    random1: int = randint(0,1)
    random2: int = randint(0,3)
    
    if random1 == 0 and size == "1": #Player stabs the zombie for 25 damage
            print(f"{ATTACK_EMOJI}")
            zpoints -= 25
            health -= zdamage
            if zpoints > 0:
                print(f"{player} stabbed the zombie for 25 damage! Current zombie health: {zpoints}")
            else:
                print(f"{player} stabbed the zombie for 25 damage, killing Level {level}'s zombie! Good job, I guess.")
                return 101
            
            print(f"{BLOOD_EMOJI}")
            print(f"Zombie hit {player} for {zdamage} health! {player}'s current health: {health}")
            return health
    elif random1 == 1 and size == "1": #Player misses the stab 
        health -= zdamage
        print(f"{player} missed! That sucks! Current zombie health: {zpoints}")
        print(f"{BLOOD_EMOJI}")
        print(f"Zombie hit {player} for {zdamage} health! {player}'s current health: {health}")
        return health

    if random2 != 3 and size == "2":
        print(f"{ATTACK_EMOJI}")
        zpoints -= 10
        health -= zdamage
        if zpoints > 0:
            print(f"{player} slashed the zombie for 10 damage! Current zombie health: {zpoints}")
        else:
            print(f"{player} slashed the zombie for 10 damage, killing Level {level}'s zombie! Good job, I guess.")
            return 101
        print(f"{BLOOD_EMOJI}")
        print(f"Zombie hit {player} for {zdamage} health! {player}'s current health: {health}")
        return health
    elif random2 == 3 and size == "2":
        health -= zdamage
        print(f"{player} missed! That sucks! Current zombie health: {zpoints}")
        print(f"{BLOOD_EMOJI}")
        print(f"Zombie hit {player} for {zdamage} health! {player}'s current health: {health}")
        return health

def heal() -> None:
    global points, zdamage, player

    print(f"Mini Shield (+10 Health, uses up 1 turn) or Shield Pot (+25 Health, uses up 2 turns)? ")
    choice: str = input("Press 1 for Mini Shield, Press 2 for Shield Pot: ")

    if choice == "1":
        if points <= 90:
            points += 10
        else:
            points = 100
        
        print(f"{HEALTH_EMOJI}")
        print(f"{player} gained +10 health! I bet that was yummy, huh?")
        points -= zdamage
        print(f"{BLOOD_EMOJI}")
        print(f"Uh oh! While {player} was busy shielding up, a zombie hit the for {zdamage} health! {player}'s current health: {points}")
    elif choice == "2":
        if points <= 75:
            points += 25
        else:
            points = 100
        
        print(f"{HEALTH_EMOJI}")
        print(f"{player} gained +25 health! You really needed that, you sickly, frail child! {player} is now at {points} health.")
        points -= zdamage
        print(f"{BLOOD_EMOJI}")
        print(f"Uh oh! While {player} was busy shielding up, a zombie hit them for {zdamage} health! {player}'s current health: {points}")
        points -= zdamage
        print(f"{BLOOD_EMOJI}")
        print(f"Too slow! {player} just got hit for {zdamage} health, again! {player}'s current health: {points}")



if __name__ == "__main__":
  main()
