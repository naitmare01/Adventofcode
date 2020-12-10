#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


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
        self.register = {}
        self.all_values = set()

    def compute(self, instructions):
        for row in instructions:
            condition = row[1]
            condition = condition.split()
            register = row[0]
            register = register.split()

            if condition[0] not in self.register:
                self.register[condition[0]] = 0
            if register[0] not in self.register:
                self.register[register[0]] = 0

            if eval(str(self.register[condition[0]]) + ''.join([str(x) for x in condition[1:]])):
                if register[1] == 'inc':
                    self.register[register[0]] += int(register[-1])
                elif register[1] == 'dec':
                    self.register[register[0]] -= int(register[-1])
            self.all_values.add(self.register[register[0]])


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = [line.strip() for line in file.readlines()]
        input_file = [x.split(' if ') for x in input_file]
    vm = VM()
    vm.compute(input_file)
    print("Part1:", max([v for k, v in vm.register.items()]))
    print("Part2:", max(vm.all_values))


if __name__ == '__main__':
    main()
