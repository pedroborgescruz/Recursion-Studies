"""
This program produces a list that contains each chunk of the string as divided
    by spaces.
November 23rd, 2021
Author: Pedro Cruz
"""
def split_string(str):
    if " " not in str:
        return [str]
    else:
        return [str[:str.index(" ")]] + split_string(str[str.index(" ")+1:])

def main():
    assert split_string("Hello there!") == ["Hello", "there!"]
    assert split_string("This_has_no_spaces") == ["This_has_no_spaces"]
    assert split_string("") == [""]
    assert split_string("ThisReturns_inAList") == ["ThisReturns_inAList"]
    assert split_string("This is bigger!") == ["This", "is", "bigger!"]

main()
