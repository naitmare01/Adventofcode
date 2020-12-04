#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from numpy import prod
from itertools import permutations


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = [int(x) for x in input_file]
    part1 = [x for x in input_file if 2020 - x in input_file]
    print("Part1:", prod(part1))

    part2 = set(permutations(input_file, 3))
    for row in part2:
        if sum(row) == 2020:
            print("Part2:", prod(row))
            break


if __name__ == '__main__':
    main()
