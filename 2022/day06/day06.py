#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

def arguments():
    '''args'''
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

def is_unique_chars(strintocheck):
    '''IsUnique'''
    # String length cannot be more than
    # 256.
    if len(strintocheck) > 256:
        return False

    # Initialize occurrences of all characters
    char_set = [False] * 128

    # For every character, check if it exists
    # in char_set
    for count, _ in enumerate(strintocheck):
        # Find ASCII value and check if it
        # exists in set.
        val = ord(strintocheck[count])
        if char_set[val]:
            return False

        char_set[val] = True

    return True


def test_is_unique(number_of_chars, input_file):
    '''Testing unique'''
    idx = 0
    while True:
        idx_end = idx + number_of_chars
        if is_unique_chars(input_file[idx:idx_end]):
            break
        idx += 1
    return idx + number_of_chars


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()

    print("Part 1:", test_is_unique(4, input_file))
    print("Part 2:", test_is_unique(14, input_file))

if __name__ == '__main__':
    main()
