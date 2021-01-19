#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
from copy import deepcopy
import time
import re


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class DragonChecksum():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.disk = None
        self.disk_size = None
        self.check_sum = None

    def fill_disk(self):
        self.disk = deepcopy(self.instructions)
        while len(self.disk) <= self.disk_size:
            append_data = deepcopy(self.disk)
            append_data = append_data[::-1]
            append_data = re.sub("1", "#", append_data)
            append_data = re.sub("0", "1", append_data)
            append_data = re.sub("#", "0", append_data)
            self.disk = (self.disk + "0" + append_data)
        self.check_sum = self.disk[0:self.disk_size]

    def calculate_checksum(self):
        while True:
            n = 2
            self.check_sum = [self.check_sum[i:i + n] for i in range(0, len(self.check_sum), n)]
            self.check_sum = ["1" if int(x) == 11 or int(x) == 0 else "0" for x in self.check_sum]
            self.check_sum = ''.join([str(elem) for elem in self.check_sum])
            if len(self.check_sum) % 2 != 0:
                break


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = str(file.read())
    dragon_checksum = DragonChecksum()
    dragon_checksum.instructions = input_file
    dragon_checksum.disk_size = 272  # 20 for demo, initial state 10000, checksum == '01100'
    dragon_checksum.fill_disk()
    dragon_checksum.calculate_checksum()
    print(f'Part1: {dragon_checksum.check_sum}')

    dragon_checksum.reset()
    dragon_checksum.disk_size = 35651584
    dragon_checksum.fill_disk()
    dragon_checksum.calculate_checksum()
    print(f'Part2: {dragon_checksum.check_sum}')

    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
