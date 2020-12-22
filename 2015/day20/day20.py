#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from functools import lru_cache
from functools import reduce
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class House():
    def __init__(self):
        self.reset()

    def reset(self):
        self.Num_Of_Presents = dict()
        self.target = None
        self.range = range(1, 5000)

    @lru_cache(maxsize=None)
    def hand_out_presents(self):
        house_id = 1
        while True:
            factor_sum = sum(self.find_all_factors(house_id))
            if self.target == factor_sum * 10:
                self.Num_Of_Presents[house_id] = self.target
                break
            else:
                house_id += 1

    def find_all_factors(self, n):
        return set(reduce(list.__add__, ([i, n / i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = int(file.read().strip())
    elves = House()
    elves.target = input_file
    elves.hand_out_presents()
    print(elves.Num_Of_Presents)
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
