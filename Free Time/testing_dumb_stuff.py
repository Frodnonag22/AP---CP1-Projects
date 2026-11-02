# Dumb stuff for me

import time
import sys
import random

def typer_print(text: str, end = "\n"):
    for char in text:
        delay = random.uniform(0.001, 0.075)
        if char == " ":
            delay = random.uniform(0.1,0.5)
        sys.stdout.write(f"{char}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

typer_print("A well-crafted paragraph is a small building block of writing that focuses on a single main idea. It starts with a clear topic sentence to introduce that idea, provides supporting details or examples in the middle, and wraps up with a smooth closing thought. When sentences flow together logically with good transitions, the whole block becomes easy to read and understand.")