#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import re


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def group_ints(times, ints):
    for n in range(times):
        temp_result = []
        for num in ints:
            number_of_iter = len(num)
            number_to_iter = num[0]
            temp_result.append(number_of_iter)
            temp_result.append(number_to_iter)
        ints = ''.join(map(str, temp_result))
        ints = [item[0] for item in re.findall(r"((.)\2*)", ints)]
    ints = ''.join(map(str, temp_result))
    return ints


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()

    grouped_ints = [item[0] for item in re.findall(r"((.)\2*)", input_file)]
    print("Part1", len(group_ints(40, grouped_ints)))
    print("Part2", len(group_ints(50, grouped_ints)))


if __name__ == '__main__':
    main()
