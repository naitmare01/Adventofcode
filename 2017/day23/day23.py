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


class VM():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.memory = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
        self.times_mul_invoked = 0

    def is_digit(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def run_vm(self):
        idx = 0
        while True:
            cmd = self.instructions[idx]
            inst = cmd[0]
            first_registrer = cmd[1]
            second_registrer = cmd[2]
            jump = 1

            if self.is_digit(second_registrer):
                value = second_registrer
            else:
                value = self.memory[second_registrer]
            
            if self.is_digit(first_registrer):
                first_value = first_registrer
            else:
                first_value = self.memory[first_registrer]

            if inst == 'set':
                self.memory[first_registrer] = int(value)
            elif inst == 'sub':
                self.memory[first_registrer] -= int(value)
            elif inst == 'mul':
                self.times_mul_invoked += 1
                self.memory[first_registrer] *= int(value)
            elif inst == 'jnz':
                if int(first_value) != 0:
                    jump = int(value)
            idx += jump
            if idx >= len(self.instructions) or idx < 0:
                break


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
        input_file = [x.split() for x in input_file]
    vm = VM()
    vm.instructions = input_file
    vm.run_vm()
    vm.instructions = input_file
    print(vm.times_mul_invoked)
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
