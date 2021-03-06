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
        self.reset()

    def reset(self):
        self.instructions = None
        self.history = []
        self.accumulator = 0
        self.accumulator_booted = 0
        self.booted = False

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

            if index == max_index:
                if instructions == 'acc':
                    self.accumulator += value
                self.booted = True
                break
            else:
                if instructions in ('nop', 'acc'):
                    index += 1
                    if instructions == 'acc':
                        self.accumulator += value
                else:
                    index += value


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = [(x[0], int(x[1])) for x in [x.split(' ') for x in input_file.splitlines()]]

    handheld = HandheldHalting()
    handheld.instructions = input_file
    handheld.boot_computer()
    print("Part1:", handheld.accumulator)

    # Part2
    index = 0
    temp_instructions = input_file
    wrong_values = {'jmp': 'nop', 'nop': 'jmp'}
    while index < len(input_file):
        handheld.reset()
        if temp_instructions[index][0] in wrong_values:
            reset_value = ([x for x, y in wrong_values.items() if x == temp_instructions[index][0]][0])
            temp_instructions[index] = (wrong_values[temp_instructions[index][0]], temp_instructions[index][1])
            handheld.instructions = temp_instructions
            handheld.boot_computer()
            if handheld.booted:
                break
            else:
                temp_instructions[index] = (reset_value, temp_instructions[index][1])
        index += 1
    print("Part2:", handheld.accumulator)


if __name__ == '__main__':
    main()
