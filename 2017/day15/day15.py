#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time
# import networkx as nx
# import collections


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class BinaryGenerator():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        return

    def parse_input(self):
        # for _ in range(80_000_000):
        #    calc = (65 * 16807) % 2147483647
        print((65 * 16807) % 2147483647)
        start = bin(65)
        factor = bin(16807)
        divider = bin(2147483647)
        print((start * factor) % divider)


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
        input_file = [x.split() for x in input_file]
    gen = BinaryGenerator()
    gen.instructions = input_file
    gen.parse_input()
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
