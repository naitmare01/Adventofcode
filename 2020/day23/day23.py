#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class CrabCups():
    def __init__(self):
        self.reset()
        self.circle = None

    def reset(self):
        self.rounds = None
        self.destination_cup = None
        self.result = None

    def play_game(self, part):
        if part == 2:
            cups = deepcopy(self.circle) + [i for i in range(len(self.circle) + 1, 1000001)]
        elif part == 1:
            cups = deepcopy(self.circle) + [i for i in range(len(self.circle) + 1, 10)]
        cups_len = len(cups)

        node_map = {}
        previous_node = None
        for cup in cups:
            node = Node(cup)
            node_map[cup] = node
            if previous_node:
                previous_node.right = node
            previous_node = node
        previous_node.right = node_map[cups[0]]

        current_node = None
        for n in range(self.rounds):
            current_node = current_node.right if current_node else node_map[cups[0]]

            picked_up = [current_node.right, current_node.right.right, current_node.right.right.right]
            current_node.right = picked_up[-1].right

            d_value = current_node.value - 1 or cups_len
            while node_map[d_value] in picked_up:
                d_value = d_value - 1 or cups_len
            self.destination_cup = node_map[d_value]

            picked_up[-1].right = self.destination_cup.right
            self.destination_cup.right = picked_up[0]

        if part == 1:
            idx = 1
            n = node_map[1]
            tmp_result = []
            while idx < len(node_map):
                tmp_result.append(n.right.value)
                n = n.right
                idx += 1
            self.result = ''.join(str(x) for x in tmp_result)
        elif part == 2:
            self.result = node_map[1].right.value * node_map[1].right.right.value


class Node():
    def __init__(self, value, right=None):
        self.value = value
        self.ref = right


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [int(x) for x in file.read()]
    crabcups = CrabCups()
    crabcups.circle = input_file
    crabcups.rounds = 100
    crabcups.play_game(1)
    print(f'Part1: {crabcups.result}')

    crabcups.reset()
    crabcups.circle = input_file
    crabcups.rounds = 10000000
    crabcups.play_game(2)
    print(f'Part2: {crabcups.result}')

    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
