#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
 }

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""
class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description


def decode_string(str):
    """Given a string named str, use the Caesar encoding above to return the decoded string."""
    # TODO: implement me
    return '1 cup'


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    # TODO: implement me
    return Ingredient("1 cup", "butter")


def main():
    """A program that decodes a secret recipe"""
    # TODO: implement me

if __name__ == "__main__":
    main()
#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
 }

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""
class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description


def decode_string(str):
    """Given a string named str, use the Caesar encoding above to return the decoded string."""
    decoded_str = ""
    for c in str:
        # obtain decoded character with the ENCODING dictionary, return the key itself if a dictionary key does not exist
        decoded_str += ENCODING.get(c, c)
    return decoded_str


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    encoded_amount, encoded_description = line.split("#")
    amount, description = decode_string(encoded_amount), decode_string(encoded_description)
    return Ingredient(amount, description)


def main():
    """A program that decodes a secret recipe"""
    file_read = open("secret_recipe.txt")
    encoded_lines = file_read.readlines()
    # iterate over each encoded_line, concatenate the decoded "amount" and "description" into one text string
    decoded_lines = [" ".join(decode_ingredient(encoded_line).__dict__.values())
                        for encoded_line in encoded_lines]
    with open("decoded_recipe.txt", "w") as file_to_write:
        file_to_write.writelines(decoded_lines)
        file_to_write.close()


if __name__ == "__main__":
    main()
