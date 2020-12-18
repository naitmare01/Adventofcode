#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
from itertools import product
# from copy import deepcopy
import time
from collections import defaultdict


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class ConwayCubes():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.start_gen = defaultdict(int)
        self.end_gen = None

    def setup_cube(self, dimensions):
        for xidx, line in enumerate(self.instructions):
            for yidx, letter in enumerate(line):
                if letter == '#':
                    self.start_gen[(xidx, yidx) + (0,) * (dimensions - 2)] = 1

    def get_all_neighbors(self, locs):
        neighbors = (self.get_neighbors(loc) for loc in locs)
        return set.union(*neighbors)

    def get_neighbors(self, loc):
        dim = len(loc)
        offsets = product((-1, 0, 1), repeat=dim)
        neighbors = set()
        for offset in offsets:
            if offset == (0,) * dim:
                continue
            neighbors.add(tuple(a + b for a, b in zip(loc, offset)))
        return neighbors

    def cycle(self, iterations):
        current_gen = self.start_gen
        for i in range(iterations):
            next_gen = defaultdict(int)
            all_locs = self.get_all_neighbors(current_gen.keys())
            all_locs.update(current_gen.keys())
            for loc in all_locs:
                neighbors = self.get_neighbors(loc)
                count = sum(current_gen[n] for n in neighbors)
                if count in (2, 3) and current_gen[loc] == 1:
                    next_gen[loc] = 1
                elif count == 3 and current_gen[loc] == 0:
                    next_gen[loc] = 1
            current_gen = next_gen
        self.end_gen = current_gen


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        # input_file = [list(map(int, line)) for line in input_file.replace('.', '0').replace('#', '1').splitlines()]
    conway = ConwayCubes()
    conway.instructions = input_file
    conway.setup_cube(3)
    conway.cycle(6)
    print(sum(conway.end_gen.values()))
    executionTime = (time.time() - startTime)
    print(f'Execution time in seconds: {executionTime}')


if __name__ == '__main__':
    main()

# https://github.com/Jozkings/advent-of-code-2020/blob/main/17.py
