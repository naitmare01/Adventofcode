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


class MemoryGame():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.last_number = None
        self.history = dict()

    def play_game(self, max_turns):
        last = -1
        for turn, number in enumerate(self.instructions):
            self.history[last], last = turn, number
        for turn in range(len(self.instructions), max_turns):
            self.history[last], last = turn, turn - self.history.get(last, turn)
        self.last_number = last


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [int(x) for x in file.read().split(',')]

    game = MemoryGame()
    game.instructions = input_file
    game.play_game(2020)
    print(f'Part1: {game.last_number}')
    game.reset()
    game.play_game(30000000)
    print(f'Part2: {game.last_number}')
    executionTime = (time.time() - startTime)
    print(f'Execution time in seconds: {executionTime}')


if __name__ == '__main__':
    main()
