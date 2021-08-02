#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class TheStarsAlign():
    def __init__(self):
        self.instructions = None


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
    print(input_file)


if __name__ == '__main__':
    main()
