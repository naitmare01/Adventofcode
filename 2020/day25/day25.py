#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
# from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class ComboBreaker():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.modulo_value = 20201227
        self.card_public_key = None
        self.door_public_key = None
        self.card_loop_size = None

    def find_card_loop_size(self, subject, public_key):
        for i in range(self.modulo_value):
            if pow(subject, i, self.modulo_value) == public_key:
                self.card_loop_size = i
        self.part1_result = pow(self.door_public_key, self.card_loop_size, self.modulo_value)


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [int(x) for x in file.read().splitlines()]
    combo = ComboBreaker()
    combo.card_public_key = input_file[0]
    combo.door_public_key = input_file[1]
    combo.find_card_loop_size(7, input_file[0])
    print(combo.part1_result)
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
