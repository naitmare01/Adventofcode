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

def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.split("\n\n")

    data = [sum([int(x) for x in y.split("\n")]) for y in input_file]
    result_pt1 = max(data)
    print("Part1:", result_pt1)

    result_pt2 = sum(sorted((data), reverse=True)[:3])
    print("Part2:", result_pt2)



if __name__ == '__main__':
    main()
