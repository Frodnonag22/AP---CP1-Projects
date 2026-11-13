# AP combat program

import sys as s
import random as r
import time as t

def clear_terminal():
    """clears the terminal"""
    print("\033[H\033[J", end="")

clear_terminal()

def cool_input(prompt: str, delay: float = 0.05):
  """Types out inputs slowly"""
  for character in prompt:
    s.stdout.write(f"{character}")
    s.stdout.flush()
    t.sleep(delay)
  return input()

red = "\033[38;5;196m"
orange = "\033[38;5;208m"
yellow = "\033[38;5;226m"
yel_green = "\033[38;5;118m"
green = "\033[38;5;46m"
cyan = "\033[38;5;51m"
blue = "\033[38;5;21m"
purple = "\033[38;5;129m"
magenta = "\033[38;5;201m"
pink = "\033[38;5;213m"
white = "\033[37m"
modifier = 0
enemy_health = 30
enemy_armor = 12
user_health = 30+modifier
user_defence = 14+modifier
starter = r.randint(1, 2)
titles = ["Brave", "Wise", "Wanderer", "DreamWeaver"]
weak_attacks = ["Stab", "Cantrip", "Crossbow Shot", "Cloud of Daggers"]
strong_attacks = ["Slash", "AoE Attack", "Dual Crossbow", "Viscious Mockery"]
simple_attacks = ["Punch", "Magic Missile", "Bow and Arrow", "Dissonant Whispers"]
name = cool_input("What is your name? ")
fight_class = int(cool_input("What fighter class are you? \n1. Fighter (Sword atacks) \n2. Mage (Magic attacks) \n3. Ranger (Ranged attacks) \n4. Bard (Little bit of all) \n"))
fleed = False

# Next 3 functions DO NOT COUNT for grading rubric
def print(text: str = "", delay: float = 0.05, end = "\n"):
    """Types out text slowly"""
    for char in text:
        s.stdout.write(f"{char}")
        s.stdout.flush()
        t.sleep(delay)
    s.stdout.write(end)
    s.stdout.flush()



def user_turn(user_health, enemy_health, fleed):
    print(f"Hello {name} the {titles[fight_class-1]}, your current stats are: \nHealth: {user_health} \nArmor Class: {user_defence} \nAttack: D20 + {modifier}")
    type_attack = int(input("What would you like to do? \n1. Normal Attack \n2. Wild Attack (Double damage, but will deal 1 D8 damage to yourself) \n3. Heal (Regain 1 D8 + 1) \n4. Flee (You may not escape) \n"))
    if type_attack == 1:
        attack = int(input(f"Do you want to \n1. {weak_attacks[fight_class-1]} (1 D8) \n2. {strong_attacks[fight_class-1]} (2 D8 + {modifier}) \n3. {simple_attacks[fight_class-1]} (4 damage)"))
        if attack == 1:
            if enemy_armor <= r.randint(1, 20+modifier):
                damage = r.randint(1, 8)
                enemy_health -= damage
                print(f"You dealt {damage} damage to the Dire Wolf")
            else:
                print("You missed")    
        elif attack == 2:
            if enemy_armor <= r.randint(1, 20+modifier):
                damage = r.randint(2, 16) + modifier
                enemy_health -= damage
                print(f"You dealt {damage} damage to the Dire Wolf")
            else:
                print("You missed")    
        else:
            if enemy_armor <= r.randint(1, 20+modifier):
                enemy_health -= 4
                print(f"You dealt 4 damage to the Dire Wolf")
            else:
                print("You missed")    
    elif type_attack == 2:
        attack = int(input(f"Do you want to \n1. {weak_attacks[fight_class-1]} (2 D8) \n2. {strong_attacks[fight_class-1]} (4 D8 + {modifier*2}) \n3. {simple_attacks[fight_class-1]} (4 damage)"))
        if attack == 1:
            if enemy_armor <= r.randint(1, 20+modifier):
                damage = r.randint(2, 16)
                enemy_health -= damage
                print(f"You dealt {damage} damage to the Dire Wolf")
            else:
                print("You missed")
            user_health -= r.randint(1, 8)
            print(f"You dealt {damage} damage to yourself")
        elif attack == 2:
            if enemy_armor <= r.randint(1, 20+modifier):
                damage = r.randint(4, 32) + (modifier*2)
                enemy_health -= damage
                print(f"You dealt {damage} damage to the Dire Wolf")
            else:
                print("You missed")
            user_health -= r.randint(1, 8)
            print(f"You dealt {damage} damage to yourself")
        else:
            if enemy_armor <= r.randint(1, 20+modifier):
                enemy_health -= 8
                print(f"You dealt 8 damage to the Dire Wolf")
            else:
                print("You missed")    
            user_health -= r.randint(1, 8)
            print(f"You dealt {damage} damage to yourself")
    elif type_attack == 3:
        user_health += r.randint(1, 8) + 1
    else:
        print("Attempting flee. . .")
        flee = r.randint(1, 10)
        if flee >= 6:
            enemy_health = 0
            fleed = True
        else: 
            pass
    return enemy_health, user_health, fleed
    
def wolf_turn(user_health, enemy_health):
    enemy_move = r.randint(1, 2)
    if enemy_move == 1:
        print("Dire wolf selected normal attack!")
        enemy_roll = r.randint(1, 20)
        enemy_attack = r.randint(1, 3)
        if enemy_attack == 1:
            if enemy_roll >= user_defence:

                user_health -= r.randint(1, 8)
        elif enemy_attack == 2:
            if enemy_roll >= user_defence:

                user_health -=  r.randint(2, 16)
        else:
            if enemy_roll >= user_defence:
                user_health -= 4
                print("Dire wolf dealt 4 damage")
    else:
        print("Dire wolf selected wild attack!")
        enemy_roll = r.randint(1, 20)
        enemy_attack = r.randint(1, 3)
        if enemy_attack == 1:
            if enemy_roll >= user_defence:
                user_health -= r.randint(1, 8)
            enemy_health -= r.randint(1,8)
        elif enemy_attack == 2:
            if enemy_roll >= user_defence:
                user_health -= r.randint(2, 16)
            enemy_health -= r.randint(1,8)
        else:
            if enemy_roll >= user_defence:
                user_health -= 8
                print("Dire wolf dealt 8 damage")
            enemy_health -= r.randint(1,8)
    return enemy_health, user_health


print("You have encountered a Dire wolf!")
while True:
    while enemy_health > 0 and user_health > 0:
        if starter%2 == 1:
            enemy_health, user_health, fleed = user_turn(user_health, enemy_health, fleed)
        else:
            enemy_health, user_health = wolf_turn(user_health, enemy_health)
        starter += 1
        if enemy_health <= 0 and fleed:
            print("You successfully fleed from the wolf")
        elif enemy_health <= 0:
            print("You have defeated the dire wolf")
            modifier += 1
        elif user_health <= 0:
            print("You died")
        else:
            pass
    play_again = input("Would you like to play again?")
    if "ye" in play_again:
        user_health = 30+modifier
        enemy_health = 30
    else:
        break