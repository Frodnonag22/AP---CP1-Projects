# AP combat program

import sys as s
import random as r
import time as t

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
enemy_health = 0
enemy_armor = 0

# Next 3 functions DO NOT COUNT for grading rubric
def print(text: str = "", delay: float = 0.05, end = "\n"):
    """Types out text slowly"""
    for char in text:
        s.stdout.write(f"{char}")
        s.stdout.flush()
        t.sleep(delay)
    s.stdout.write(end)
    s.stdout.flush()

def cool_input(prompt: str, delay: float = 0.05):
  """Types out inputs slowly"""
  for character in prompt:
    s.stdout.write(f"{character}")
    s.stdout.flush()
    t.sleep(delay)
  return input()

def clear_terminal():
    """clears the terminal"""
    print("\033[H\033[J", end="")

clear_terminal()

def user_turn():
    if fight_class == 1:
        user_health = 30+modifier
        user_defence = 14+modifier
        print(f"Hello {name} the Brave, your current stats are: \nHealth: 30 \nArmor Class: {user_defence} \nAttack: D20 + {modifier}")
        type_attack = int(input("What would you like to do? \n1. Normal Attack \n2. Wild Attack (Double damage, but will deal 1 D8 damage to yourself) \n3. Heal (Regain 1 D8 + 1) \n4. Flee (You may not escape) \n"))
        if type_attack == 1:
            attack = int(input(f"Do you want to \n1. Stab (1 D8) \n2. Slash (2 D8 + {modifier}) \n3. Punch (4 damage)"))
            if attack == 1:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    damage = r.randint(1, 8)
                    enemy_health -= damage
            elif attack == 2:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    damage = r.randint(2, 16) + modifier
                    enemy_health -= damage
            else:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    enemy_health -= 4
        elif type_attack == 2:
            attack = int(input(f"Do you want to \n1. Stab (2 D8) \n2. Slash (4 D8 + {modifier*2}) \n3. Punch (4 damage)"))
            if attack == 1:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    enemy_health -= r.randint(2, 16)
                user_health -= r.randint(1, 8)
            elif attack == 2:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    enemy_health -= r.randint(4, 32) + (modifier*2)
                user_health -= r.randint(1, 8)
            else:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    enemy_health -= 8
                user_health -= r.randint(1, 8)
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
    if fight_class == 2:
        user_health = 30+modifier
        user_defence = 14+modifier
        print(f"Hello {name} the Wise, your current stats are: \nHealth: {user_health} \nArmor Class: {user_defence} \nAttack: D20 + {modifier}")
        type_attack = int(cool_input("What would you like to do? \n1. Normal Attack \n2. Wild Attack (Double damage, but will deal 1 D8 damage to yourself) \n3. Heal (Regain 1 D8 + 1) \n4. Flee (You may not escape) \n"))
        if type_attack == 1:
            attack = int(cool_input(f"Do you want to \n1. Cantrip (1 D8) \n2. AoE Blast (2 D8 + {modifier}) \n3. Magic Missile (4 damage)"))
            if attack == 1:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    damage = r.randint(1, 8)
                    enemy_health -= damage
            elif attack == 2:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    damage = r.randint(2, 16) + modifier
                    enemy_health -= damage
            else:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    enemy_health -= 4
        elif type_attack == 2:
            attack = int(cool_input(f"Do you want to \n1. Cantrip (2 D8) \n2. AoE Blast (4 D8 + {modifier*2}) \n3. Magic Missile (4 damage)"))
            if attack == 1:
                enemy_health -= r.randint(2, 16)
                user_health -= r.randint(1, 8)
            elif attack == 2:
                enemy_health -= r.randint(4, 32) + (modifier*2)
                user_health -= r.randint(1, 8)
            else:
                enemy_health -= 8
                user_health -= r.randint(1, 8)
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
    if fight_class == 3:
        user_health = 30+modifier
        user_defence = 14+modifier
        print(f"Hello {name} the Pathfinder, your current stats are: \nHealth: {user_health} \nArmor Class: {user_defence} \nAttack: D20 + {modifier}")
        type_attack = int(cool_input("What would you like to do? \n1. Normal Attack \n2. Wild Attack (Double damage, but will deal 1 D8 damage to yourself) \n3. Heal (Regain 1 D8 + 1) \n4. Flee (You may not escape) \n"))
        if type_attack == 1:
            attack = int(cool_input(f"Do you want to \n1. Crossbow Shot (1 D8) \n2. Dual Crossbow Shot (2 D8 + {modifier}) \n3. Bow & Arrow (4 damage)"))
            if attack == 1:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    damage = r.randint(1, 8)
                    enemy_health -= damage
            elif attack == 2:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    damage = r.randint(2, 16) + modifier
                    enemy_health -= damage
            else:
                if enemy_armor > r.randint(1, 20+modifier):
                    pass
                else:
                    enemy_health -= 4
        elif type_attack == 2:
            attack = int(cool_input(f"Do you want to \n1. Crossbow Shot (2 D8) \n2. Dual Crossbow Shot (4 D8 + {modifier*2}) \n3. Bow & Arrow (4 damage)"))
            if attack == 1:
                enemy_health -= r.randint(2, 16)
                user_health -= r.randint(1, 8)
            elif attack == 2:
                enemy_health -= r.randint(4, 32) + (modifier*2)
                user_health -= r.randint(1, 8)
            else:
                enemy_health -= 8
                user_health -= r.randint(1, 8)
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

name = cool_input("What is your name? ")
fight_class = int(cool_input("What fighter class are you? \n1. Fighter (Sword atacks) \n2. Mage (Magic attacks) \n3. Ranger (Ranged attacks) \n4. Bard (Little bit of all) \n"))
fleed = False

user_turn()