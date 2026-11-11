"""Problem 2: binary search (no built-in search).

Input:  line 1 -> n
        line 2 -> n sorted integers
        line 3 -> target
Output: 0-based index of target, or -1 if it is not present.
"""
import sys


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    arr = list(map(int, tokens[1:1 + n]))
    target = int(tokens[1 + n])
    print(binary_search(arr, target))
