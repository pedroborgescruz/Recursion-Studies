"""
This program computes the sum of the first N integers.
November 23rd, 2021
Author: Pedro Cruz
"""

def first_integers(n):
    if n == 0:
        return 0
    else:
        return n + first_integers(n-1)

def main():
    assert first_integers(3) == 6
    assert first_integers(7) == 28
    assert first_integers(0) == 0
    assert first_integers(10) == 55
    assert first_integers(20) == 210

main()
