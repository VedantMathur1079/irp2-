"""Problem 1: reverse the word order of a line read from standard input."""
import sys


def reverse_words(line):
    return " ".join(reversed(line.split()))


if __name__ == "__main__":
    print(reverse_words(sys.stdin.readline()))
