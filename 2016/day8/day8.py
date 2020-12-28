#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
# from copy import deepcopy
import time
import numpy as np
# import hashlib


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Grid():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        # self.screen = [[0 for i in range(50)] for j in range(6)]
        self.screen = np.zeros((6, 50))
        self.number_of_lit_pixels = 0

    def run_program(self):
        for line in self.instructions:
            inst = line.split()
            if inst[0] == 'rect':
                x, y = inst[-1].split('x')
                x, y = int(x), int(y)
                for xcord in range(x):
                    for ycord in range(y):
                        self.screen[ycord][xcord] = 1
            elif inst[0] == 'rotate':
                steps_to_rotate = int(inst[4])
                if inst[1] == 'row':
                    row_to_rotate = int(inst[2].split('y=')[1])
                    self.screen[row_to_rotate] = np.roll(self.screen[row_to_rotate], steps_to_rotate)
                else:
                    col_to_rotate = int(inst[2].split('x=')[1])
                    self.screen = np.transpose(self.screen)
                    self.screen[col_to_rotate] = np.roll(self.screen[col_to_rotate], steps_to_rotate)
                    self.screen = np.transpose(self.screen)
        self.number_of_lit_pixels = int(np.sum(self.screen))


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
    grid = Grid()
    grid.instructions = input_file
    grid.run_program()
    print(f'Part1: {grid.number_of_lit_pixels}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
