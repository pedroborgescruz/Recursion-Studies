"""
This program returns a new list that excludes (filters out) any numbers in the
    original list that are larger than max_value.
November 23rd, 2021
Author: Pedro Cruz
"""

def filter_larger_than(lst, max_value):
    if lst == []:
        return []
    else:
        if lst[0] > max_value:
            return filter_larger_than(lst[1:], max_value)
        else:
            return lst[:1]  + filter_larger_than(lst[1:], max_value)

def main():
    assert filter_larger_than([7, 2, 5, 4, 6, 3], 5) == [2, 5, 4, 3]
    assert filter_larger_than([100, 200, 300], 10) == []
    assert filter_larger_than([], 15) == []
    assert filter_larger_than([5, 5, 5, 5], 4) == []

main()
