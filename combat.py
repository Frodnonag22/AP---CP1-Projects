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
name = input("What is your name? ")
fight_class = input("What fighter class are you? \n1. Fighter (Sword atacks) \n2. Mage (Magic attacks) \n3. Ranger (Ranged attacks) \n4. Bard (Little bit of all) \n")

# Next 3 functions DO NOT COUNT for grading rubric
def print(text: str = "", delay: float = 0.05, end = "\n"):
    """Types out text slowly"""
    for char in text:
        s.stdout.write(f"{char}")
        s.stdout.flush()
        t.sleep(delay)
    s.stdout.write(end)
    s.stdout.flush()

def input(prompt: str, delay: float = 0.05):
  """Types out inputs slowly"""
  for character in prompt:
    s.stdout.write(f"{character}")
    s.stdout.flush()
    t.sleep(delay)
  return input()

def clear_terminal():
    """clears the terminal"""
    print("\033[H\033[J", end="")

def user_turn():
    if fight_class == 1:
        user_health = 30
        user_defence = 14
        print(f"Hello {name} the Brave, your stats are: \nHealth: 30")
        type_attack = int(input("What would you like to do? \n1. Normal Attack \n2. Wild Attack (Double damage, but will deal 1 D8 damage) \n3. Heal (Regain 1 D8 + 1) \n Flee (You may not escape) \n"))
        if type_attack == 1:
            attack = int(input(f"Do you want to \n1. Stab (2 D8) \n2. Slash (1 D8 + {modifier}) \n3. Punch (guaranteed 4 damage)"))
            if attack == 1:
                damage = r.randint(2,16)
                enemy_health -= damage
            elif attack == 2:
                damage = r.randint(1,8) + modifier
                enemy_health -= damage
            else:
                enemy_health -= 4
        elif type_attack == 2:
            attack = int(input(f"Do you want to \n1. Stab (4 D8) \n2. Slash (2 D8 + {modifier*2}) \n3. Punch (guaranteed 4 damage)"))
            if attack == 1:
                damage = r.randint(4,32)
                enemy_health -= damage
            elif attack == 2:
                damage = r.randint(2,16) + (modifier*2)
                enemy_health -= damage
            else:
                enemy_health -= 8
        else:

training = input("Do you want to practice before a real fight? ")

if "ye" in training:
   user_turn()