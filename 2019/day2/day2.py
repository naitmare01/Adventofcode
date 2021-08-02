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
        self.noun_verb_range = 100
        self.wanted = None

    def compute(self, part2):
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

                if part2:
                    if self.instructions[0] == self.wanted:
                        return True


def main():
    args = arguments()

    with open(args.file) as file:
        file = list(file.read().split(','))
        input_file = [int(x) for x in file]
    intcode_computer = computer()
    intcode_computer.instructions = list(input_file)
    intcode_computer.compute(False)
    part1_answer = intcode_computer.instructions[0]
    print("Part1:", part1_answer)

    for noun in range(100):
        for verb in range(100):
            intcode_computer.reset()
            intcode_computer.wanted = 19690720
            intcode_computer.instructions = list(input_file)
            intcode_computer.instructions[1] = noun
            intcode_computer.instructions[2] = verb
            if intcode_computer.compute(True):
                print("Part2:", 100 * noun + verb)


if __name__ == '__main__':
    main()
