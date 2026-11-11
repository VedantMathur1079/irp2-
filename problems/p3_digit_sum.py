"""Problem 3: sum of digits using recursion only (no loops)."""
import sys


def digit_sum(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


if __name__ == "__main__":
    print(digit_sum(int(sys.stdin.readline())))
