#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from functools import reduce


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class CustomCustoms():
    def __init__(self):
        self.answers = None
        self.answers_pt2 = None

    def find_anwers_pt1(self, group):
        self.answers = (len(set(group.replace("\n", ""))))


def part2(input_path):
    return sum(
        [
            len(reduce(lambda set_1, set_2: set_1.intersection(set_2), [set(word) for word in g if word])) for g in
            [group.split('\n') for group in open(input_path).read().split('\n\n')]
        ])


def main():
    args = arguments()
    with open(args.file) as file:
        print("Part2:", part2(args.file))
        input_file = file.read().strip().split("\n\n")
    result = []
    for row in input_file:
        custom_answers = CustomCustoms()
        custom_answers.find_anwers_pt1(row)
        result.append(custom_answers)
    print("Part1:", sum([x.answers for x in result]))


if __name__ == '__main__':
    main()
