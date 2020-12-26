#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
# from copy import deepcopy
# from itertools import product


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Board():
    def __init__(self):
        self.reset()

    def reset(self):
        self.grid = None
        self.living = set()

    def find_living_cells(self):
        for rowidx, x in enumerate(self.grid):
            for colidx, y in enumerate(x):
                if y == 1:
                    self.living.add((rowidx, colidx))
        self.max_x = len(self.grid) - 1
        self.max_y = len(self.grid[0]) - 1

    def check_neighbour(self, cell):
        x, y = cell
        yield x - 1, y - 1
        yield x, y - 1
        yield x + 1, y - 1
        yield x - 1, y
        yield x + 1, y
        yield x - 1, y + 1
        yield x, y + 1
        yield x + 1, y + 1

    def apply_iteration(self, board):
        new_board = set([])
        candidates = board.union(set(n for cell in board for n in self.check_neighbour(cell)))
        for cell in candidates:
            x, y = cell
            if x > self.max_x or x < 0:
                continue
            if y > self.max_y or y < 0:
                continue
            count = sum((n in board) for n in self.check_neighbour(cell))
            if count == 3 or (count == 2 and cell in board):
                new_board.add(cell)
        self.living = new_board


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read()
        input_file = [list(map(int, line)) for line in input_file.replace('.', '0').replace('#', '1').splitlines()]

    board = Board()
    board.grid = input_file
    board.find_living_cells()
    number_of_iterations = 100
    for _ in range(number_of_iterations):
        board.apply_iteration(board.living)
    print(f'Part1: {len(board.living)}')


if __name__ == '__main__':
    main()
