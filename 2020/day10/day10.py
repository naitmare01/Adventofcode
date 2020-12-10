#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class AdapterArray():
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None
        self.charging_outlet = 0
        self.answers = []

    def chain(self):
        self.answers = ([y - x for x, y in zip(self.instructions[:-1], self.instructions[1:])])
        self.answers.append(3)


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = [int(line.strip()) for line in file.readlines()]
        input_file.append(0)
        input_file = sorted(input_file)
    adapters = AdapterArray()
    adapters.instructions = input_file
    adapters.chain()
    part1_answer = len([x for x in adapters.answers if x == 3]) * len([x for x in adapters.answers if x == 1])
    print("Part1:", part1_answer)


if __name__ == '__main__':
    main()
