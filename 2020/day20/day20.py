#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from functools import lru_cache
from itertools import permutations
# from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class JurassicJigsaw():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.tiles = dict()
        self.all_combinations = set()

    @lru_cache
    def setup_tiles(self):
        for tile in self.instructions:
            tile_id = int(tile[0].split(' ')[1].split(':')[0])
            self.tiles[tile_id] = tile[1:]
        self.all_combinations = set(permutations(list(self.tiles.keys())))


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [x.splitlines() for x in file.read().split('\n\n')]
    jigsaw = JurassicJigsaw()
    jigsaw.instructions = input_file
    jigsaw.setup_tiles()
    print(jigsaw.tiles.keys())
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
