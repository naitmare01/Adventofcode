#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
# from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Ticket():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.extra_attr = dict()
        self.scanning_error = list()
        self.valid_pt1 = False

    def set_extra_attr(self, attributes):
        for attr in attributes:
            self.extra_attr[attr] = True

    def check_valid(self, plane):
        for ticket in self.instructions:
            tmp_valid = list()
            for n in (plane.capacity):
                if any(ticket in x for x in plane.capacity[n]):
                    tmp_valid.append(True)
                else:
                    tmp_valid.append(False)
                # for idx, cap in enumerate(plane.capacity[n]):
                #    print(n, idx, (ticket in cap))
            if all(x is False for x in tmp_valid):
                self.scanning_error.append(ticket)
                self.extra_attr[n] = False
        if len(self.scanning_error) == 0:
            self.valid_pt1 = True


class Plane():
    def __init__(self):
        self.reset()

    def reset(self):
        self.capacity = dict()
        self.instructions = None

    def set_capacity(self):
        for attr in self.instructions:
            capacity_detail = (attr.split(': '))
            values = capacity_detail[1].split(' or ')
            range1, range2 = [int(x) for x in values[0].split('-')], [int(x) for x in values[1].split('-')]
            self.capacity[capacity_detail[0]] = (range(range1[0], range1[1] + 1), range(range2[0], range2[1] + 1))


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.split('\n\n')
        input_file = [x.splitlines() for x in input_file]

    result = []
    plane = Plane()
    plane.instructions = input_file[0]
    plane.set_capacity()
    for row in input_file[2][1:]:
        ticket = Ticket()
        ticket.instructions = [int(x) for x in row.split(',') if x.isdigit()]
        ticket.set_extra_attr(plane.capacity)
        ticket.check_valid(plane)
        result.append(ticket)
    part1_result = sum([sum([y for y in x]) for x in [x.scanning_error for x in result]])
    print(f'Part1: {part1_result}')

    part2 = [x for x in result if x.valid_pt1 is True]
    col_input = list(zip(*[[int(y) for y in x.split(',')] for x in (input_file[2][1:])]))
    print(col_input)
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
