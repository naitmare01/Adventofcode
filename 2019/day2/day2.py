#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class computer():
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None

    def compute(self):
        for index in range(0, len(self.instructions), 4):
            operator = self.instructions[index]

            if operator == 99:  # Halting
                return
            else:
                first_input = self.instructions[self.instructions[index + 1]]
                second_input = self.instructions[self.instructions[index + 2]]

                if operator == 1:  # Addition
                    new_result = first_input + second_input
                elif operator == 2:  # Multiplication
                    new_result = first_input * second_input

                self.instructions[self.instructions[index + 3]] = new_result


def main():
    args = arguments()

    with open(args.file) as file:
        file = list(file.read().split(','))
        input_file = map(int, file)
    intcode_computer = computer()
    intcode_computer.instructions = list(input_file)
    intcode_computer.compute()
    part1_answer = intcode_computer.instructions[0]
    print("Part1:", part1_answer)


if __name__ == '__main__':
    main()
