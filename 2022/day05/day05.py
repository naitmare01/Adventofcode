#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import re

def arguments():
    '''args'''
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

def read_file():
    '''Read File'''
    args = arguments()
    with open(args.file, 'r', encoding="utf8") as file:
        file_data = file.read()
        definition, moves = file_data.split('\n\n')
        containers = []

        for line in definition.split('\n')[: -1]:
            replace = ' [0]'

            if line[0] == ' ':
                replace = '[0] '

            containers.append(line.replace('    ', replace).split())

        max_len = max([len(line) for line in containers])

        for line in containers:
            t = max_len - len(line)
            if t > 0:
                line += ['[0]'] * t
        t = []

        for i in range(len(containers[0])):
            y = []
            for j in range(len(containers)):
                if containers[j][i] != '[0]':
                    y.append(containers[j][i])
            t.append(y)

        pattern = r'^move (\d+) from (\d+) to (\d+)$'

        # [(qty, src, dst)...]
        instruction_list = [list(map(lambda x: int(x), re.findall(pattern, line)[0])) for line in
                            moves.strip().split('\n')]

        return t, instruction_list


class SupplyStacks():
    '''Supplystack'''
    def __init__(self):
        self.supply_stacks = None

    def rearrange(self, instructions):
        '''Rearrange'''
        for row in instructions:
            number_of_crates_to_move, from_stack, to_stack = row[0], row[1], row[2]
            for _ in range(number_of_crates_to_move):
                moved_stacks = (self.supply_stacks[from_stack - 1].pop(0))
                self.supply_stacks[to_stack - 1].insert(0, moved_stacks)


def main():
    '''Main'''
    data, inst = read_file()
    supply_stacks = SupplyStacks()
    supply_stacks.supply_stacks = data
    supply_stacks.rearrange(inst)
    part1_result = ([x[0] for x in supply_stacks.supply_stacks])
    part1_result = "".join(part1_result)
    part1_result = part1_result.replace('[', '').replace(']', '')

    print("Part1:", part1_result)


if __name__ == '__main__':
    main()
