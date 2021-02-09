#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time
# import networkx as nx
# import collections
# from math import sqrt
# from itertools import count, islice


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Node():
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left


class Knot():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.node_map = dict()
        self.current_posistion = 0
        self.skip_size = 0

    def setup_ring(self, values):
        node = None
        for x in values:
            if node is None:
                node = Node(x)
                self.node_map[x] = node
            else:
                new_node = Node(x)
                node.right = new_node
                self.node_map[x] = new_node
                node = new_node
        self.node_map[values[-1]].right = self.node_map[values[0]]

        node = None
        for n in values:
            if node is None:
                node = len(values) - 1
            else:
                node = n - 1
            self.node_map[n].left = self.node_map[node]


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().split(',')
        input_file = [int(x) for x in input_file]
    knot = Knot()
    knot.instructions = input_file
    knot.setup_ring([0, 1, 2, 3, 4])  # Sample input
    for k, v in knot.node_map.items():
        print("left", v.left.value, "Middle", k, "Right", v.right.value)

    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
