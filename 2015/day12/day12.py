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


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()

    all_numbers = [int(d) for d in re.findall(r'-?\d+', input_file)]
    print(sum(all_numbers))


if __name__ == '__main__':
    main()
