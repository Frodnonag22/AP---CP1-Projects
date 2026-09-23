# Andrew Petersen Free Time 

# Text Styles
reset = "\033[0m"
bold ="\033[1m"
dim = "\033[2m"
itailc = "\033[3m"
underline = "\033[4m"
blink = "\033[5m"
invert = "\033[7m"
strike = "\033[9m"

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

bg_red = "\033[41m"
bg_green = "\033[42m"
bg_yellow = "\033[43m"
bg_blue = "\033[44m"
bg_magenta = "\033[45m"
bg_cyan = "\033[46m"
bg_white = "\033[47m"
bg_dark_grey = "\033[100m"

def smoothly_simulated_blink(text: str, loop_count: int = 4) -> None:
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
    print(f"\r{bold}{red}⚠️ ALERT: {text}{reset}")

# Example usage
print(f"{red}This text is red!{reset}")
print(f"{green}This text is green!{reset}")
print(f"Normal text, {yellow}yellow text{reset}, normal text.")

def matrix_rainbow_typewriter(text: str, delay: float = 0.04) -> None:
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

matrix_rainbow_typewriter("Decryption pipeline processing... Access Granted.")
print()
smoothly_simulated_blink("Unauthorized database intrusion detected!")