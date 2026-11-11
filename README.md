# IRP-II Assignment 5: Git/GitHub and DSA Problems in Python

- **Name:** Vedant Mathur
- **Roll No:** 2481228

## Problems

| File | Problem |
|---|---|
| `problems/p1_reverse_words.py` | Reverse the word order of a line |
| `problems/p2_binary_search.py` | Binary search (no built-in search), prints 0-based index or -1 |
| `problems/p3_digit_sum.py` | Digit sum using recursion only |
| `problems/p4_pair_count.py` | Count pairs `i < j` with `a[i] + a[j] == k` |

Problem 4: the assignment text was cut off after "count pairs i", so the standard version (pairs `i < j` summing to `k`) is assumed.

## How to run

Needs Python 3. Every program reads from standard input.

```bash
python problems/p1_reverse_words.py < tests/p1_reverse_words/input_1.txt
python problems/p2_binary_search.py < tests/p2_binary_search/input_1.txt
python problems/p3_digit_sum.py < tests/p3_digit_sum/input_1.txt
python problems/p4_pair_count.py < tests/p4_pair_count/input_1.txt
```

You can also type the input yourself, for example `echo "I love coding" | python problems/p1_reverse_words.py`.

## Tests

Each folder in `tests/` has `input_N.txt` and `expected_N.txt` pairs. Run them all with:

```bash
python run_tests.py
```

## Branches

Work was done on `dev` and merged into `main`.
