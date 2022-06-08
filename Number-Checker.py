"""
This program checks if an item is contained in a list.
November 23rd, 2021
Author: Pedro Cruz
"""

def contains_number(lst, n):
    if lst == []:
        return False
    else:
        if lst[0] != n:
            return contains_number(lst[1:], n)
        else:
            return True

def main():
    lst = [2, 3, 5]
    assert contains_number(lst, 3) == True
    assert contains_number(lst, 7) == False
    assert contains_number([1, 3, 5, 7], 7) == True
    assert contains_number([2, 5, 8, 9, 5, 2, 1], 0) == False
    assert contains_number(lst, 22) == False

main()
