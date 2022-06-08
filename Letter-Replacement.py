"""
This program produces a new string in which all instances of the target letter
    are replaced by the replacement letter.
November 23rd, 2021
Author: Pedro Cruz
"""

def replace_letter(str, target_char, new_char):
    if str == "":
        return ""
    else:
        if str[0] == target_char:
            return new_char + replace_letter(str[1:], target_char, new_char)
        else:
            return str[0] + replace_letter(str[1:], target_char, new_char)

def main():
    assert replace_letter("hello", "e", "o") == "hollo"
    s = "Now is the best time"
    assert replace_letter(s, "e", "a") == "Now is tha bast tima"
    assert replace_letter("", "s", "z") == ""
    t = "Hello world!"
    assert replace_letter(t, "l", "") == "Heo word!"
    assert replace_letter("ana", "a", "n") == "nnn"

main()
