#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import itertools


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

    part1 = []
    for n in range(len(input_file)):
        if n == 0:
            continue
        part1.append(list(((itertools.permutations(input_file, n + 1)))))

    for row in part1:
        for line in row:
            if sum(line) == 25:
                print(line)


if __name__ == '__main__':
    main()
