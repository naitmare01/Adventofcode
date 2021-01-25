#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time
# import re


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Rouge():
    def __init__(self):
        self.reset()
        self.instructions = []
        self.cols = 0

    def reset(self):
        return

    def find_next_row(self, x):
        new_row = list()
        x -= 1
        for y, y_ in enumerate(self.instructions[-1]):
            trap = False
            center = self.instructions[x][y]
            if y == 0:
                right = self.instructions[x][y + 1]
                if right == '^':
                    trap = True

            elif y == self.cols - 1:
                left = self.instructions[x][y - 1]
                if left == '^':
                    trap = True
            else:
                left = self.instructions[x][y - 1]
                right = self.instructions[x][y + 1]
                if left == '^' and right != '^' and center == '^':
                    trap = True

                if right == '^' and left != '^' and center == '^':
                    trap = True

                if right == '^' and left != '^' and center != '^':
                    trap = True

                if left == '^' and right != '^' and center != '^':
                    trap = True
            if trap:
                new_row.append('^')
            else:
                new_row.append('.')
        self.instructions.append(new_row)


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = [x for x in input_file]
    rouge = Rouge()
    rouge.cols = len(input_file)
    rouge.instructions.append(input_file)
    for n in range(39):
        rouge.find_next_row(n + 1)

    part1_result = (sum([len([y for y in x if y == '.']) for x in rouge.instructions]))
    print(f'Part1: {part1_result}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
