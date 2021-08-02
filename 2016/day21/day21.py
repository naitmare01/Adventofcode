#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Scramble():
    def __init__(self):
        self.reset()
        self.instructions = None
        self.letters = None

    def reset(self):
        None

    def run_scramble(self):
        for row in self.instructions:
            inst = row[0]
            if inst == 'swap':
                print(row)


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
        input_file = [x.split() for x in input_file]
    input_letter = "abcde"
    scramble = Scramble()
    scramble.letters = input_letter
    scramble.instructions = input_file
    scramble.run_scramble()


if __name__ == '__main__':
    main()
