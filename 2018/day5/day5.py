#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Polymer: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    def __init__(self):
        self.name = None
        self.result_part1 = None
        self.result_part2 = []
        self.unique_letters = None

    def reactions(self, text):
        stack_result = []
        for letter in text:
            last_letter = stack_result[-1] if stack_result else None
            if letter != last_letter and (last_letter == letter.upper() or last_letter == letter.lower()):
                stack_result.pop()
            else:
                stack_result.append(letter)
        self.result_part1 = stack_result

    def get_unique_letters(self, text):
        self.unique_letters = set(text.lower())

    def reactions_part2(self, text):
        result_part2 = []
        for word in text:
            Polymer.reactions(self, word)
            result_part2.append(len(self.result_part1))
        self.result_part2 = min(result_part2)

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
    list_polymer = list(input_file)
    polymer = Polymer()
    polymer.reactions(list_polymer)
    print("part1:", len(polymer.result_part1))

    #part2
    polymer.get_unique_letters(input_file)
    removed_letters_polymer = (list(input_file.replace(c, "").replace(c.upper(), "") for c in polymer.unique_letters))
    polymer.reactions_part2(removed_letters_polymer)
    print("part2:", polymer.result_part2)

if __name__ == '__main__':
    main()
