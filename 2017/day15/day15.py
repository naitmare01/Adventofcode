#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time
# import networkx as nx
# import collections


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class BinaryGenerator():
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None
        self.name = None
        self.factor = None
        self.divider = None
        self.starting_value = None
        self.current_value = None
        self.bin_current_value = None

    def generate(self):
        if self.current_value is None:
            self.current_value = self.starting_value
        self.current_value = self.current_value * self.factor
        self.current_value = self.current_value % self.divider

        self.bin_current_value = bin(self.current_value).replace("0b", "")
        self.bin_current_value = self.bin_current_value[-16:]


def solve(ga, gb, iterations, needs_multiple):
    count = 0
    for i in range(iterations):
        while True:
            ga *= 16807
            ga %= 2147483647
            if not needs_multiple or ga % 4 == 0:
                break
        while True:
            gb *= 48271
            gb %= 2147483647
            if not needs_multiple or gb % 8 == 0:
                break
        if (ga & 65535 == gb & 65535):
            count += 1
    return count


print(solve(591, 393, 40_000_000, False))
print(solve(591, 393, 5_000_000, True))


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
        input_file = [x.split() for x in input_file]
    generators = []
    for gen in input_file:
        bingen = BinaryGenerator()
        bingen.instructions = gen
        bingen.name = bingen.instructions[1]
        bingen.divider = 2147483647
        bingen.starting_value = int(bingen.instructions[4])
        if bingen.name == 'A':
            bingen.factor = 16807
        else:
            bingen.factor = 48271
        generators.append(bingen)

    part1 = 0
    for i in range(1):
        for bin_gen in generators:
            bin_gen.generate()
        if len((set([(x.bin_current_value) for x in generators]))) == 1:
            part1 += 1
    print("Part1:", part1)
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))


if __name__ == '__main__':
    main()
