#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Submarine:
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None
        self.horizontal_position = 0
        self.depth = 0
        self.result_pt1 = 0

    def move_submarine(self):
        for row in self.instructions:
            dir, val = row[0], int(row[1])
            if dir == 'forward':
                self.horizontal_position += val
            elif dir == 'down':
                self.depth += val
            elif dir == 'up':
                self.depth -= val
        self.result_pt1 = self.horizontal_position * self.depth


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = [x.split() for x in input_file]
    sub = Submarine()
    sub.instructions = input_file
    sub.move_submarine()
    print("Part1:", sub.result_pt1)


if __name__ == '__main__':
    main()
