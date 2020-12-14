#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class VM():
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None
        self.mem = dict()
        self.mask = None
        self.mem_int = dict()

    def get_bin(self, x, n):
        return format(x, 'b').zfill(n)

    def update_memory(self):
        for row in self.instructions:
            if row.startswith('mem'):
                instruc = row.split(' = ')
                mem_value = int(instruc[-1])
                mem_location = int((instruc[0])[3:].replace('[', '').replace(']', ''))

                mask_replaces_ones = [idx for idx, x in enumerate(self.mask) if x == '1']
                mask_replaces_zeroes = [idx for idx, x in enumerate(self.mask) if x == '0']

                temp = self.get_bin(mem_value, 36)
                res = ['1' if idx in mask_replaces_ones else ele for idx, ele in enumerate(temp)]
                res = ['0' if idx in mask_replaces_zeroes else ele for idx, ele in enumerate(res)]
                self.mem[mem_location] = ''.join(res)
            else:
                self.mask = (row.split(' = '))[-1]

        self.mem_int = deepcopy(self.mem)
        for bin_mem in self.mem_int:
            self.mem_int[bin_mem] = int(self.mem_int[bin_mem], 2)


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.splitlines()
    vm = VM()
    vm.instructions = input_file
    vm.update_memory()
    print("Part1:", sum(vm.mem_int.values()))

    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))


if __name__ == '__main__':
    main()
