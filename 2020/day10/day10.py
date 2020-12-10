#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from functools import lru_cache


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
        self.total_distinct_ways = None

    def chain(self):
        self.answers = ([y - x for x, y in zip(self.instructions[:-1], self.instructions[1:])])
        self.answers.append(3)

    @lru_cache(maxsize=None)
    def find_all_combs(self, idx, last):
        if 1 < self.instructions[idx] - last < 3:
            return 0
        if idx == len(self.instructions) - 1:
            return 1
        else:
            possible = [(idx, x) for (idx, x) in enumerate(self.instructions[idx:idx + 4]) if 1 <= x - last <= 3]
            return sum([self.find_all_combs(idx + poss[0], poss[1]) for poss in possible])


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
    part2_answer = adapters.find_all_combs(0, input_file[0])
    print("Part1:", part1_answer)
    print("Part2:", part2_answer)


if __name__ == '__main__':
    main()
