#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

def arguments():
    '''args'''
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def return_is_range(range1_start, range1_stop, range2_start, range2_stop):
    '''range'''
    if set((range(range1_start, range1_stop))).issubset(range(range2_start, range2_stop)):
        return True
    elif set((range2_start, range2_stop)).issubset(range(range1_start, range1_stop)):
        return True
    else:
        return False


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = [x.split(',') for x in input_file]
        input_file = [[(y.split('-')) for y in x] for x in input_file]
    part1_data = [return_is_range(int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])) for line in input_file]

    print("Part1:", sum(part1_data))

if __name__ == '__main__':
    main()
