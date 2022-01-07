#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from os import stat
from copy import deepcopy
from collections import Counter


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
        input_file = input_file.split(',')
        input_file = [int(x) for x in input_file]
    pt2input_file = deepcopy(input_file)

    for y in range(80):
        for n, fish in enumerate(input_file):
            if fish == 0:
                input_file.append(9)
                input_file[n] = 6
            else:
                input_file[n] -= 1
    print("Part1:", len(input_file))

    lifes = dict(Counter(pt2input_file))
    for day in range(256):
        lifes = {l: (0 if lifes.get(l+1) is None else lifes.get(l+1)) for l in range(-1, 8)}
        lifes[8] = lifes[-1]
        lifes[6] += lifes[-1]
        lifes[-1] = 0
    print("Part2:", sum(lifes.values()))


if __name__ == '__main__':
    main()
