#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import itertools


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class EncodingError():
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None
        self.preamble = None
        self.chunck_size = None
        self.encoded_msg_pt1 = None
        self.encoded_msg_pt2 = None

    def encode(self):
        for n in range(self.preamble, len(self.instructions)):
            if self.instructions[n] not in [x + y for x, y in itertools.combinations(self.instructions[n - self.preamble:n], self.chunck_size)]:
                self.encoded_msg_pt1 = self.instructions[n]
                break

        for n in range(len(self.instructions)):
            sums = [sum(self.instructions[n:a]) for a in range(len(self.instructions) - n)]
            if self.encoded_msg_pt1 in sums:
                position = sums.index(self.encoded_msg_pt1)
                self.encoded_msg_pt2 = int(min(self.instructions[n:position]) + int(max(self.instructions[n:position])))


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = [int(line.strip()) for line in file.readlines()]

    encode = EncodingError()
    encode.instructions = input_file
    encode.preamble = 25
    encode.chunck_size = 2
    encode.encode()
    print("Part1:", encode.encoded_msg_pt1)
    print("Part2:", encode.encoded_msg_pt2)


if __name__ == '__main__':
    main()
