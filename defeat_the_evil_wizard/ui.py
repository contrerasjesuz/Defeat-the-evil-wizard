import sys
import time


def slow_print(text, delay=0.03, newline=True):
    # Printing text like it's being typed.
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()
