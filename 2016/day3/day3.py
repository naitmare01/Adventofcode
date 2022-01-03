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


def checkValidity(a, b, c):
    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


def slice_per(source, step):
    return [source[i::step] for i in range(step)]


def main():
    args = arguments()

    day1data = []
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        for row in input_file:
            day1data.append((re.sub("\s+", ",", row.strip()).split(',')))

    day1_result = 0
    for triangle in day1data:
        if checkValidity(int(triangle[0]), int(triangle[1]), int(triangle[2])):
            day1_result += 1

    print("Part1:", day1_result)

    part2data = (','.join(([','.join(x) for x in day1data])))
    part2data = part2data.split(',')
    part2data = slice_per(part2data, 3)
    part2data = (','.join(([','.join(x) for x in part2data])))
    part2data = part2data.split(',')
    part2data = [part2data[x: x + 3] for x in range(0, len(part2data), 3)]

    part2_result = 0
    for triangle in part2data:
        if checkValidity(int(triangle[0]), int(triangle[1]), int(triangle[2])):
            part2_result += 1

    print("Part2:", part2_result)


if __name__ == '__main__':
    main()
