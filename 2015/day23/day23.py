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
        self.instructions = None

    def reset(self):
        self.memory = {'a': 0, 'b': 0}

    def write_memory(self):
        idx = 0
        while idx < len(self.instructions):
            line = self.instructions[idx]
            cmd = line[0]
            if cmd == 'inc':  # inc r increments register r, adding 1 to it, then continues with the next instruction.
                self.memory[line[1]] += 1
                idx += 1
            elif cmd == 'hlf':  # hlf r sets register r to half its current value, then continues with the next instruction.
                half = int(self.memory[line[1]] / 2)
                if half < 0:
                    half == 0
                self.memory[line[1]] = half
                idx += 1
            elif cmd == 'tpl':  # tpl r sets register r to triple its current value, then continues with the next instruction.
                self.memory[line[1]] = int(self.memory[line[1]] * 3)
                idx += 1
            elif cmd == 'jmp':  # jmp offset is a jump; it continues with the instruction offset away relative to itself.
                idx += int(line[1])
            elif cmd == 'jie':  # jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
                register = line[1][0]
                if self.memory[register] % 2 == 0:
                    idx += int(line[2])
                else:
                    idx += 1
            elif cmd == 'jio':  # jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
                register = line[1][0]
                if self.memory[register] == 1:
                    idx += int(line[2])
                else:
                    idx += 1


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
        input_file = [x.split() for x in input_file]

    vm = VM()
    vm.instructions = input_file
    vm.write_memory()
    print(f'Part1: {vm.memory["b"]}')


if __name__ == '__main__':
    main()
