#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from copy import deepcopy


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class VMReplacements():
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None
        self.molecule = None
        self.encoded_molecule = set()

    def parse_instrcutions(self):
        self.molecule = self.instructions.pop()
        self.instructions = [x.split(' => ') for x in self.instructions]

    def encode_molecule(self):
        for instruction in self.instructions:
            for idx, character in enumerate(self.molecule):
                if instruction[0] == character:
                    temp_molecule = deepcopy(self.molecule)
                    temp_molecule = temp_molecule[:idx] + instruction[-1] + temp_molecule[idx + 1:]
                    self.encoded_molecule.add(temp_molecule)


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = [line.strip() for line in file.readlines()]
        input_file = [x for x in input_file if x != ""]

    vm = VMReplacements()
    vm.instructions = input_file
    vm.parse_instrcutions()
    vm.encode_molecule()
    print("Part1:", len(vm.encoded_molecule))


if __name__ == '__main__':
    main()
