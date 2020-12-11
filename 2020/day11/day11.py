#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from copy import deepcopy
from functools import lru_cache


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class SeatingSystem():
    def __init__(self):
        self.reset()

    def reset(self):
        self.seats = None
        self.part1 = True
        self.answer = 0

    @lru_cache(maxsize=None)
    def change_seats(self):
        while True:
            rows = len(self.seats)
            cols = len(self.seats[0])
            temp_seats = deepcopy(self.seats)
            change = False
            for row in range(rows):
                for col in range(cols):
                    change_threshold = 0
                    for drow in [-1, 0, 1]:
                        for dcol in [-1, 0, 1]:
                            if not (drow == 0 and dcol == 0):
                                adjrow = row + drow
                                adjcol = col + dcol

                                while 0 <= adjrow < rows and 0 <= adjcol < cols and self.seats[adjrow][adjcol] == '.' and (not self.part1):
                                    adjrow = adjrow + drow
                                    adjcol = adjcol + dcol
                                if (0 <= adjrow < rows) and (0 <= adjcol < cols) and (self.seats[adjrow][adjcol] == '#'):
                                    change_threshold += 1

                    if self.seats[row][col] == 'L':
                        if change_threshold == 0:
                            temp_seats[row][col] = '#'
                            change = True
                    elif self.seats[row][col] == '#' and change_threshold >= (4 if self.part1 else 5):
                        temp_seats[row][col] = 'L'
                        change = True
            if not change:
                break

            self.seats = deepcopy(temp_seats)

        for row in range(rows):
            for col in range(cols):
                if self.seats[row][col] == '#':
                    self.answer += 1


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = list(map(list, input_file.splitlines()))
    seating = SeatingSystem()
    seating.seats = input_file
    seating.change_seats()
    print("Part1:", seating.answer)

    seating = SeatingSystem()
    seating.seats = input_file
    seating.part1 = False
    seating.change_seats()
    print("Part2:", seating.answer)


if __name__ == '__main__':
    main()
