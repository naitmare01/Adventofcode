#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from functools import lru_cache
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
        self.black_tiles = set()

    def flip_tiles(self):
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
                if tile in self.black_tiles:
                    self.tiles[tile] = 'white'
                    self.black_tiles.remove(tile)
                else:
                    self.tiles[tile] = 'black'
                    self.black_tiles.add(tile)
            else:
                self.tiles[tile] = 'black'
                self.black_tiles.add(tile)

    def get_neighbors(self, tile):
        return [tuple([tile[i] + d[i] for i in range(3)]) for d in [(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1), (0, -1, 1)]]

    @lru_cache(maxsize=None)
    def conway_tiles(self):
        for _ in range(100):
            next_black = set()
            for tile in self.black_tiles:
                ns = self.get_neighbors(tile)
                count_black = 0
                for n in ns:
                    if n in self.black_tiles:
                        count_black += 1
                if 0 < count_black <= 2:
                    next_black.add(tile)
                for n in ns:
                    if n in self.black_tiles:
                        continue
                    n_of_ns = self.get_neighbors(n)
                    count_black = 0
                    for n_of_n in n_of_ns:
                        if n_of_n in self.black_tiles:
                            count_black += 1
                    if count_black == 2:
                        next_black.add(n)
            self.black_tiles = {i for i in next_black}


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
    lobby = LobbyLayout()
    lobby.instructions = input_file
    lobby.flip_tiles()
    part1_result = len(lobby.black_tiles)
    print(f'Part1: {part1_result}')
    lobby.conway_tiles()
    part2_result = len(lobby.black_tiles)
    print(f'Part2: {part2_result}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
