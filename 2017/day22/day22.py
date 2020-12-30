#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from functools import lru_cache
# from itertools import permutations
from copy import deepcopy
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
    def __init__(self, value, right=None, left=None, forward=None, right_facing=None, left_facing=None):
        self.value = value
        self.right = right
        self.left = left
        self.forward = forward
        self.left_facing = left_facing
        self.right_facing = right_facing


class InfectedNodes():
    def __init__(self, value, weaken=None):
        self.value = value
        self.weaken = weaken
        # self.flag = flag


class VirusCarrier():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.facing = 'U'
        self.movement = dict()
        self.coordinations = list()
        self.infected_nodes = None
        self.infected_values = None
        self.number_of_burst_infected = 0
        self.setup_movement_maps()

    def setup_movement_maps(self):
        # Facing, left, right, left_facing, right_facing
        # facings = [('U', [0, -1], [0, 1]), ('R', [-1, 0], [1, 0]), ('D', [0, 1], [0, -1]), ('L', [1, 0], [-1, 0])]
        facings = [('U', [0, -1], [0, 1], [-1, 0]), ('R', [-1, 0], [1, 0], [0, 1]), ('D', [0, 1], [0, -1], [1, 0]), ('L', [1, 0], [-1, 0], [0, -1])]
        for fac in facings:
            node = Node(fac[0])
            node.right = fac[2]
            node.left = fac[1]
            node.forward = fac[3]
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

    @lru_cache(maxsize=None)
    def move_pt2(self, turns):
        for _ in range(turns):
            if self.coordinations[0] not in self.infected_nodes:
                # Clean node, proceed to weaken, turn left, move forward
                self.infected_nodes[self.coordinations[0]] = self.infected_values['clean'].weaken
                new_facing = self.movement[self.facing].left_facing.value
                movement_steps = self.movement[self.facing].left
            else:
                node_status = self.infected_nodes[self.coordinations[0]]
                if node_status.value == 'weakened':
                    # weakened node, weaken, dont turn, move forward
                    self.infected_nodes[self.coordinations[0]] = self.infected_nodes[self.coordinations[0]].weaken
                    movement_steps = self.movement[self.facing].forward
                    self.number_of_burst_infected += 1
                elif node_status.value == 'infected':
                    # infected node, weaken, turn right, move forward
                    self.infected_nodes[self.coordinations[0]] = self.infected_nodes[self.coordinations[0]].weaken
                    new_facing = self.movement[self.facing].right_facing.value
                    movement_steps = self.movement[self.facing].right
                elif node_status.value == 'flagged':
                    # flagged node, clean(remove from self.infected_nodes), turn twice(180) and move
                    del self.infected_nodes[self.coordinations[0]]
                    new_facing = self.movement[self.facing].left_facing.left_facing.value
                    movement_steps = self.movement[new_facing].forward

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
        self.infected_values = dict()
        self.grid_pt2 = dict()
        self.middle = None

    def setup_grid(self):
        # declare circular list manually.
        self.infected_values['clean'] = InfectedNodes('clean')
        self.infected_values['weakened'] = InfectedNodes('weakened')
        self.infected_values['infected'] = InfectedNodes('infected')
        self.infected_values['flagged'] = InfectedNodes('flagged')

        self.infected_values['clean'].weaken = self.infected_values['weakened']
        self.infected_values['weakened'].weaken = self.infected_values['infected']
        self.infected_values['infected'].weaken = self.infected_values['flagged']
        self.infected_values['flagged'].weaken = self.infected_values['clean']

        for xcord, row in enumerate(self.instructions):
            for ycord, col in enumerate(row):
                if self.instructions[xcord][ycord] == '#':  # infected
                    self.grid.add((xcord, ycord))
                    self.grid_pt2[(xcord, ycord)] = self.infected_values['infected']
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
    player.coordinations = deepcopy(grid.middle)
    player.infected_nodes = grid.grid
    player.move(10000)
    print(f'Part1: {player.number_of_burst_infected}')

    # Part2
    player.reset()
    player.coordinations = deepcopy(grid.middle)
    player.infected_nodes = grid.grid_pt2
    player.infected_values = grid.infected_values
    player.move_pt2(10000000)
    print(f'Part2: {player.number_of_burst_infected}')

    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
