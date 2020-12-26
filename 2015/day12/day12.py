#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import re
import json


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def calculate(json_data):
    if type(json_data) == int:
        return json_data
    if type(json_data) == list:
        return sum([calculate(json_data) for json_data in json_data])
    if type(json_data) != dict:
        return 0
    if 'red' in json_data.values():
        return 0
    return calculate(list(json_data.values()))


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()

    all_numbers = [int(d) for d in re.findall(r'-?\d+', input_file)]
    print("Part1:", sum(all_numbers))
    all_numbers_part2 = json.loads(input_file)
    print("Part2:", calculate(all_numbers_part2))


if __name__ == '__main__':
    main()
