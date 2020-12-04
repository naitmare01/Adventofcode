#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import hashlib


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

    decimal = 0
    while True:
        str2hash = input_file + str(decimal)
        result = hashlib.md5(str2hash.encode())
        leading_zeroes = (result.hexdigest())[0:5]
        if leading_zeroes == "00000":
            print("Part1:", decimal)
            break
        else:
            decimal += 1

    decimal = 0
    while True:
        str2hash = input_file + str(decimal)
        result = hashlib.md5(str2hash.encode())
        leading_zeroes = (result.hexdigest())[0:6]
        if leading_zeroes == "000000":
            print("Part2:", decimal)
            break
        else:
            decimal += 1


if __name__ == '__main__':
    main()
