#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
# from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class LobbyLayout():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.directions = {'e': (1, -1, 0), 'se': (0, -1, 1), 'sw': (-1, 0, 1), 'w': (-1, 1, 0), 'nw': (0, 1, -1), 'ne': (1, 0, -1)}  # x,y,z
        self.reference_point = (0, 0, 0)
        self.tiles = dict()

    def parse_input(self):
        for line in self.instructions:
            idx = 0
            tile = (0, 0, 0)
            while idx < len(line):
                if line[idx] == 'e':
                    add_cord = (self.directions['e'])
                    idx += 1
                elif line[idx] == 'w':
                    add_cord = self.directions['w']
                    idx += 1
                else:
                    add_cord = self.directions[line[idx:idx + 2]]
                    idx += 2
                tile = tuple(map(sum, zip(add_cord, tile)))

            if self.tiles.get(tile):
                if self.tiles[tile] == 'black':
                    self.tiles[tile] = 'white'
                else:
                    self.tiles[tile] = 'black'
            else:
                self.tiles[tile] = 'black'


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
    lobby = LobbyLayout()
    lobby.instructions = input_file
    lobby.parse_input()
    part1_result = len([v for k, v in lobby.tiles.items() if v == 'black'])
    print(f'Part1: {part1_result}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
