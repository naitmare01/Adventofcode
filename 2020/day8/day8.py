#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class HandheldHalting():
    def __init__(self):
        self.instructions = None
        self.history = []
        self.accumulator = 0

    def boot_computer(self):
        index = 0
        while True:
            if index in self.history:
                break
            else:
                self.history.append(index)

            instructions = self.instructions[index][0]
            value = self.instructions[index][1]
            max_index = len(self.instructions) - 1

            if instructions == 'nop':
                if index == max_index:
                    index = 0
                else:
                    index += 1

            if instructions == 'acc':
                if index == max_index:
                    index = 0
                else:
                    index += 1
                    self.accumulator += value

            if instructions == 'jmp':
                if value == max_index:
                    index -= 1
                elif value > max_index:
                    remainder = (value % max_index) - 1
                    index += remainder
                else:
                    if (index + value) > max_index:
                        difference = abs(max_index - (index + value)) - 1
                        index = difference
                    elif (index + value) < max_index:
                        index += value


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = [x.split(' ') for x in input_file]
        input_file = [(x[0], int(x[1])) for x in input_file]

    handheld = HandheldHalting()
    handheld.instructions = input_file
    handheld.boot_computer()
    print("Part1:", handheld.accumulator)
    # print([x for x in input_file if x == ('nop', 0)])


if __name__ == '__main__':
    main()
