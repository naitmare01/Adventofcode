#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time
# import networkx as nx
# import collections
# import numpy as np


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Node():
    def __init__(self, value, right=None, left=None, right_facing=None, left_facing=None):
        self.value = value
        self.right = right
        self.left = left
        self.left_facing = left_facing
        self.right_facing = right_facing


class VirusCarrier():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.facing = 'U'
        self.movement = {}  # {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        self.coordinations = list()
        self.infected_nodes = None
        self.number_of_burst_infected = 0

    def setup_movement_maps(self):
        # Facing, left, right, left_facing, right_facing
        facings = [('U', [0, -1], [0, 1]), ('R', [-1, 0], [1, 0]), ('D', [0, 1], [0, -1]), ('L', [1, 0], [-1, 0])]
        for fac in facings:
            node = Node(fac[0], fac[2], fac[1])
            self.movement[fac[0]] = node

        # declare circular list manually.
        self.movement['U'].left_facing = self.movement['L']
        self.movement['U'].right_facing = self.movement['R']

        self.movement['R'].left_facing = self.movement['U']
        self.movement['R'].right_facing = self.movement['D']

        self.movement['D'].left_facing = self.movement['R']
        self.movement['D'].right_facing = self.movement['L']

        self.movement['L'].left_facing = self.movement['D']
        self.movement['L'].right_facing = self.movement['U']

    def move(self, turns):
        for _ in range(turns):
            if (self.coordinations[0]) in self.infected_nodes:
                new_facing = self.movement[self.facing].right_facing.value
                movement_steps = self.movement[self.facing].right
                self.infected_nodes.remove(self.coordinations[0])
            else:
                new_facing = self.movement[self.facing].left_facing.value
                self.infected_nodes.add(self.coordinations[0])
                self.number_of_burst_infected += 1
                movement_steps = self.movement[self.facing].left
            new_x = movement_steps[0] + self.coordinations[0][0]
            new_y = movement_steps[1] + self.coordinations[0][1]
            self.facing = new_facing
            self.coordinations[0] = (new_x, new_y)


class Grid():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.grid = set()
        self.middle = None

    def setup_grid(self):
        for xcord, row in enumerate(self.instructions):
            for ycord, col in enumerate(row):
                if self.instructions[xcord][ycord] == '#':  # infected
                    self.grid.add((xcord, ycord))
        middlex = (len(self.instructions[0]) - 1) / 2
        middley = (len(self.instructions) - 1) / 2
        self.middle = [(int(middlex), int(middley))]


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
    grid = Grid()
    grid.instructions = input_file
    grid.setup_grid()
    player = VirusCarrier()
    player.coordinations = grid.middle
    player.infected_nodes = grid.grid
    player.setup_movement_maps()
    player.move(10000)
    print(f'Part1: {player.number_of_burst_infected}')

    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
