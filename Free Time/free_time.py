# Andrew Petersen Free Time

import sys
import time

# Text Styles
reset = "\033[0m"
bold ="\033[1m"
dim = "\033[2m"
itailc = "\033[3m"
underline = "\033[4m"
blink = "\033[5m"
invert = "\033[7m"
strike = "\033[9m"

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
black = "\033[38;5;16m"
white = "\033[37m"

def smoothly_simulated_blink(text: str, loop_count: int = 4):
    """Guaranteed cross-platform blinking text using carriage returns (\r)."""
    print(f"{bold}Initializing Simulated Hardware Alert Loop...{reset}")
    
    for _ in range(loop_count):
        # Write text and remain on the same line string block
        sys.stdout.write(f"\r{bold}{red}⚠️ ALERT: {text}{reset}")
        sys.stdout.flush()
        time.sleep(0.4)
        
        # Completely obscure the line by writing empty spaces over the string length
        sys.stdout.write("\r" + " " * (len(text) + 10))
        sys.stdout.flush()
        time.sleep(0.3)
        
    # Leave final state cleanly visible 
    print(f"\r{bold}{red}⚠️  ALERT: {text}{reset}")

# Example usage
print(f"{red}This text is red!{reset}")
print(f"{green}This text is green!{reset}")
print(f"Normal text, {yellow}yellow text{reset}, normal text.")

def matrix_rainbow_typewriter(text: str, delay: float = 0.04):
    """Prints text character by character cycling through an RGB color wheel."""
    # Custom 24-bit RGB neon spectrum
    colors = [
        (255, 0, 0),    # red
        (255, 127, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (139, 0, 255)   # Violet
    ]
    
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        # Construct dynamic 24-bit color string
        color_code = f"\033[1;38;2;{r};{g};{b}m"
        
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
        
    print(reset)

def less_cool_print(text: str, delay: float = 0.05): # cool_print(text, delay)
    """Prints text character by character cycling through an RGB color wheel."""
    # Custom 24-bit RGB neon spectrum if wanted
    colors = [(255, 255, 255)]
    
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        # Construct dynamic 24-bit color string
        color_code = f"\033[1;38;2;{r};{g};{b}m"
        
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
        
    print(reset)

# Use these in every assignmet now
def cool_print(text: str, delay: float = 0.05, end = "\n"):
    for char in text:
        sys.stdout.write(f"{char}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def cool_input(prompt: str, delay: float = 0.05):
  for character in prompt:
    sys.stdout.write(f"{character}")
    sys.stdout.flush()
    time.sleep(delay)
  return input()

def clear_terminal():
    print("\033[H\033[J", end="")

#This is when you can write your code!

matrix_rainbow_typewriter("Decryption pipeline processing... Access Granted.")
less_cool_print(f"Decryption pipeline processing... Access Denied.", 0.05)
print()
smoothly_simulated_blink("Unauthorized database intrusion detected!")
cool_print("TTERTERTERETRETERTERTRe", 0.05)

print(f"I am going to ask you for 3 numbers, these are for the color of your choice")
color_1 = input("Give me a number between 0 and 255: ")
color_2 = input("Give me a number between 0 and 255: ")
color_3 = input("Give me a number between 0 and 255: ")

def choice_matrix_typewriter(text: str, delay: float = 0.04) -> None:
    """Prints text character by character cycling through an RGB color wheel."""
    # Custom 24-bit RGB neon spectrum
    colors = [
        (color_1, color_2, color_3),
    ]
    
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        # Construct dynamic 24-bit color string
        color_code = f"\033[1;38;2;{r};{g};{b}m"
        
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
        
    print(reset)

choice_matrix_typewriter(f"Decryption pipeline processing... Access.")