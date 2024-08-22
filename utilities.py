import sys
import time


def type_text(text, delay=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def lines(length):
    print('=' * length)
