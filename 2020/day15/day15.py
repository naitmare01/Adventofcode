#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
from copy import deepcopy
import time
from collections import defaultdict


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class MemoryGame():
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None
        self.last_number = None

    def play_game(self, max_turns):
        hist = defaultdict(lambda: turn)
        last = -1
        for turn, number in enumerate(self.instructions):
            hist[last], last = turn, int(number)
        for turn in range(len(self.instructions), max_turns):
            hist[last], last = turn, turn - hist[last]
        self.last_number = last


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.split(',')
        input_file = [int(x) for x in input_file]

    game = MemoryGame()
    game.instructions = deepcopy(input_file)
    game.play_game(2020)
    print("Part1:", game.last_number)
    game.reset()
    game.instructions = deepcopy(input_file)
    game.play_game(30000000)
    print("Part2:", game.last_number)
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))


if __name__ == '__main__':
    main()
