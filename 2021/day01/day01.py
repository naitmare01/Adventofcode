#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def test_increase(list_of_ints):
    times_of_increases = 0
    for index, elem in enumerate(list_of_ints):
        prev_el = list_of_ints[index-1]
        if elem > prev_el:
            times_of_increases += 1
    return times_of_increases


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = [int(x) for x in input_file]

    part1 = test_increase(input_file)
    print("Part1:", part1)

    # Part 2
    pt2list = []
    for index, elem in enumerate(input_file):
        try:
            input_file[index+2]
            new_number = sum(input_file[index:index+3])
            pt2list.append(new_number)
        except IndexError:
            test = 'null'

    part2 = test_increase(pt2list)
    print("Part2:", part2)


if __name__ == '__main__':
    main()
