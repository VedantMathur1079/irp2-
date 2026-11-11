"""Problem 4: count pairs.

The assignment text for this problem was cut off after "count pairs i".
Assumption used here (the standard version of this problem):
count pairs of indices i < j such that a[i] + a[j] == k.

Input:  line 1 -> n and k
        line 2 -> n integers
Output: the number of such pairs.

Runs in O(n): for each element, add how many earlier elements equal k - x.
"""
import sys


def count_pairs(arr, k):
    seen = {}
    count = 0
    for x in arr:
        count += seen.get(k - x, 0)
        seen[x] = seen.get(x, 0) + 1
    return count


if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    n, k = int(tokens[0]), int(tokens[1])
    arr = list(map(int, tokens[2:2 + n]))
    print(count_pairs(arr, k))
