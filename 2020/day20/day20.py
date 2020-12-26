#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time
# import numpy as np


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Tile:
    def __init__(self, tile: list[str], tile_id: int = 0):
        self.tile = tile
        self.id = tile_id
        self.edge_len = len(tile)

    def right_edge(self) -> str:
        return ''.join(t[-1] for t in self.tile)

    def left_edge(self) -> str:
        return ''.join(t[0] for t in self.tile)

    def top_edge(self) -> str:
        return self.tile[0]

    def bottom_edge(self) -> str:
        return self.tile[-1]

    def rotate_right(self):
        rotated = []
        for ix in range(self.edge_len):
            rotated.append(''.join([
                self.tile[self.edge_len - jx - 1][ix]
                for jx in range(self.edge_len)
            ]))
        self.tile = rotated

    def flip(self):
        flipped = []
        for t in reversed(self.tile):
            flipped.append(t)
        self.tile = flipped

    def remove_edge(self):
        removed = []
        for ix in range(1, self.edge_len - 1):
            removed.append(''.join([
                self.tile[ix][jx]
                for jx in range(1, self.edge_len - 1)
            ]))
        self.tile = removed


class JurassicJigsaw():
    def __init__(self):
        self.reset()

    def reset(self):
        self.tiles = None
        self.result_pt1 = None

    def part1(self):
        size = len(self.tiles)
        edge_size = int(size ** 0.5)
        order = recursion([], set(), self.tiles, edge_size)

        upper_left = 0
        upper_right = edge_size - 1
        bottom_left = size - edge_size
        bottom_right = size - 1

        self.result_pt1 = order[upper_left].id * order[upper_right].id * order[bottom_left].id * order[bottom_right].id


def check(order: list[Tile], tile: Tile, edge_size: int) -> bool:
    if len(order) + 1 - edge_size > 0:
        if tile.top_edge() != order[len(order) - edge_size].bottom_edge():
            return False
    if (len(order) + 1) % edge_size != 1:
        if tile.left_edge() != order[len(order) - 1].right_edge():
            return False
    return True


reassemble = [
    lambda tile: tile,
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.flip(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
]


def recursion(order, visited, tiles, edge_size) -> list[Tile]:
    if len(order) == len(tiles):
        return order

    for tile in tiles:
        if tile not in visited:
            for r in reassemble:
                r(tile)
                if check(order, tile, edge_size):
                    result = recursion(order + [tile], visited.union({tile}), tiles, edge_size)
                    if result:
                        return result


def setup_tiles(lines) -> list[Tile]:
    tile_id, tile = -1, []
    tiles = []
    for line in lines:
        if 'Tile' in line:
            tile_id = int(line[5:-1])
            tile = []
        elif line:
            tile.append(line)
            is_square = len(tile) == len(tile[0])
            if is_square:
                tiles.append(Tile(tile, tile_id))
    return tiles


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [line for line in file.read().splitlines()]
    jigsaw = JurassicJigsaw()
    jigsaw.tiles = setup_tiles(input_file)
    jigsaw.part1()
    print(jigsaw.result_pt1)
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
