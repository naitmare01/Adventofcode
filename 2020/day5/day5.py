#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class BoardingPass():
    def __init__(self):
        self.row = None
        self.column = None
        self.id = None

    def find_seat(self, seat):
        all_rows = [x for x in range(128)]
        all_columns = [x for x in range(8)]
        for idx, instruction in enumerate(seat):
            if idx <= 6:
                keep_value = int(len(all_rows) / 2)
                if instruction == "F":
                    all_rows = all_rows[:keep_value]
                elif instruction == "B":
                    all_rows = all_rows[keep_value:]
            else:
                keep_value = int(len(all_columns) / 2)
                if instruction == "L":
                    all_columns = all_columns[:keep_value]
                elif instruction == "R":
                    all_columns = all_columns[keep_value:]
        self.row = all_rows[0]
        self.column = all_columns[0]
        self.id = self.row * 8 + self.column


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
    result = []
    for row in input_file:
        boarding = BoardingPass()
        boarding.find_seat(row)
        result.append(boarding)
    print("Part1:", max([x.id for x in result]))


if __name__ == '__main__':
    main()
