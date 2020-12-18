#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import product
# from copy import deepcopy
import time
# from collections import defaultdict


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Integer(object):
    def __init__(self, val=0):
        self._val = int(val)

    def __add__(self, val):
        if isinstance(val, Integer):
            return Integer(self._val + val._val)
        return self._val + val

    def __iadd__(self, val):
        self._val += val
        return self

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return 'Integer(%s)' % self._val

    def __sub__(self, val):
        return self.val * val


class VM():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.memory = dict()
        self.max = 65535

    def add_to_memory(self, key_to_add):
        self.memory[key_to_add] = 0

    def store_memory(self):
        for row in self.instructions:
            bit_instruction = row.split()

            if not self.memory.get(bit_instruction[-1]):
                self.add_to_memory(bit_instruction[-1])

            if bit_instruction[1] == '->' and bit_instruction[0].isdigit():
                self.memory[bit_instruction[-1]] = int(bit_instruction[0])
            elif bit_instruction[1] == 'AND':
                if not self.memory.get(bit_instruction[0]):
                    self.add_to_memory(bit_instruction[0])
                if not self.memory.get(bit_instruction[2]):
                    self.add_to_memory(bit_instruction[2])
                self.memory[bit_instruction[-1]] += self.memory[bit_instruction[0]] & self.memory[bit_instruction[2]]
            elif bit_instruction[1] == 'OR':
                if not self.memory.get(bit_instruction[0]):
                    self.add_to_memory(bit_instruction[0])
                if not self.memory.get(bit_instruction[2]):
                    self.add_to_memory(bit_instruction[2])
                self.memory[bit_instruction[-1]] += self.memory[bit_instruction[0]] | self.memory[bit_instruction[2]]
            elif bit_instruction[1] == 'LSHIFT':
                if not self.memory.get(bit_instruction[0]):
                    self.add_to_memory(bit_instruction[0])
                self.memory[bit_instruction[-1]] += self.memory[bit_instruction[0]] << int(bit_instruction[2])
            elif bit_instruction[1] == 'RSHIFT':
                if not self.memory.get(bit_instruction[0]):
                    self.add_to_memory(bit_instruction[0])
                self.memory[bit_instruction[-1]] += self.memory[bit_instruction[0]] >> int(bit_instruction[2])
            elif bit_instruction[0] == 'NOT':
                if not self.memory.get(bit_instruction[1]):
                    self.add_to_memory(bit_instruction[1])
                complement = ~self.memory[bit_instruction[1]]
                if complement < 0:
                    complement = (self.max - abs(complement)) + 1
                self.memory[bit_instruction[-1]] += complement
            else:
                print(bit_instruction)


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.splitlines()
    vm = VM()
    vm.instructions = input_file
    vm.store_memory()
    print([vm.memory[x] for x in vm.memory if x == 'a'])
    print([vm.memory[x] for x in vm.memory if x == 'lx'])
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
