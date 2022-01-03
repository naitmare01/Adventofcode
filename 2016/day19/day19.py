#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class ElfGame():
    def __init__(self):
        self.reset()
        self.instructions = None
        self.node_map = {}

    def reset(self):
        return

    def setup_cirlce(self):
        previous_node = None
        for cup in self.instructions:
            node = Node(cup)
            self.node_map[cup] = node
            if previous_node:
                previous_node.right = node
            previous_node = node
        previous_node.right = self.node_map[self.instructions[0]]

    def play_game(self):
        current_elf = self.node_map.keys()
        current_elf = next(iter(self.node_map))
        current_elf = self.node_map[current_elf]
        while len(self.node_map) > 1:
            elf_to_remove = current_elf.right
            new_neighbour = elf_to_remove.right
            current_elf.right = new_neighbour
            current_elf = new_neighbour
            del self.node_map[elf_to_remove.value]


class Node():
    def __init__(self, value, right=None):
        self.value = value
        self.ref = right


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = int(file.read())
        input_file = [x for x in range(input_file + 1) if x != 0]
    elfgame = ElfGame()
    elfgame.instructions = input_file
    elfgame.setup_cirlce()
    elfgame.play_game()
    result = [k for k in elfgame.node_map.keys()][0]
    print(f'Part1: {result}')

    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
