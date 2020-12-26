#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from functools import reduce
from itertools import combinations
from operator import mul


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Plane():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.num_groups = None
        self.result = None

    def find_groups(self):
        group_size = sum(self.instructions) // self.num_groups
        for i in range(len(self.instructions)):
            qes = [reduce(mul, c) for c in combinations(self.instructions, i) if sum(c) == group_size]
            if qes:
                self.result = min(qes)
                return


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
        input_file = [int(x) for x in input_file]

    plane = Plane()
    plane.instructions = input_file
    plane.num_groups = 3
    plane.find_groups()
    print(f'Part1: {plane.result}')
    plane.reset()
    plane.num_groups = 4
    plane.find_groups()
    print(f'Part2: {plane.result}')


if __name__ == '__main__':
    main()
