#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
from copy import deepcopy
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

    def tie_knot(self):
        for cmd in self.instructions:
            # node_list = list(self.node_map)
            if cmd == 1:
                print("value is 1 do somethin")
                continue
            # old_begin = self.node_map[node_list[self.current_posistion]]
            # old_end = deepcopy(old_begin)
            # for n in range(cmd):
            #    old_end = old_end.right
            # old_end = self.node_map[node_list[cmd - 1]]
            # print(old_begin.value, old_end.value, cmd)
            # new_begin_left = deepcopy(old_end.left)
            # new_begin_rigth = deepcopy(old_end.right)
            # new_end_left = deepcopy(old_begin.left)
            # new_end_right = deepcopy(old_begin.right)

            # old_begin.left.right = old_end
            # old_end.right.left = old_begin

            # old_begin.left = new_begin_left
            # old_begin.right = new_begin_rigth
            # old_end.left = new_end_left
            # old_end.right = new_end_right
            # self.current_posistion += cmd + self.skip_size


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().split(',')
        input_file = [int(x) for x in input_file]
    knot = Knot()
    knot.instructions = input_file
    knot.setup_ring([0, 1, 2, 3, 4])  # Sample input
    knot.tie_knot()
    for k, v in knot.node_map.items():
        print("left", v.left.value, "Middle", k, "Right", v.right.value)

    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()

# Register usage:
# a is debug flag
# h is counter
# f is a flag
# g is work reg
# b is starting number
# c is ending number
# e is inner loop variable
# d is outer loop variable
