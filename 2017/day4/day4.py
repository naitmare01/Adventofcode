#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Passphrases: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self):
        self.number_of_valid_phrases_simple = 0
        self.number_of_valid_phrases_advanced = 0

    def validate_passphrase(self, list_of_passphrases):
        for phrase in list_of_passphrases:
            if len(phrase) == len(set(phrase)):
                self.number_of_valid_phrases_simple = self.number_of_valid_phrases_simple + 1

            advance_phrase = ""
            phrase = [sorted(x) for x in phrase]
            phrase = [advance_phrase.join(x) for x in phrase]

            if len(phrase) == len(set(phrase)):
                self.number_of_valid_phrases_advanced = self.number_of_valid_phrases_advanced + 1

def main():
    args = arguments()
    work_list = []

    with open(args.file) as file:
        input_file = file.read().strip().split("\n")
        for row in input_file:
            work_list.append(row.split(" "))

        pass_phrases = Passphrases()
        pass_phrases.validate_passphrase(work_list)
        print("part1:", pass_phrases.number_of_valid_phrases_simple)
        print("part2:", pass_phrases.number_of_valid_phrases_advanced)

if __name__ == '__main__':
    main()
