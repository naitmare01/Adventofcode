#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class CrabCups():
    def __init__(self):
        self.reset()

    def reset(self):
        self.circle = None
        self.rounds = 100
        self.current_cup = None
        self.current_cup_idx = None
        self.destination_cup = None
        self.destination_cup_idx = None
        self.result = None

    def play_game(self):
        cups = deepcopy(self.circle)
        self.current_cup = None
        cups_len = len(cups)

        for i in range(self.rounds):
            self.current_cup_idx = (cups.index(self.current_cup) + 1) % cups_len if self.current_cup else 0
            self.current_cup = cups[self.current_cup_idx]

            picked_up = []
            for j in range(3):
                picked_up.append(cups[(self.current_cup_idx + j + 1) % cups_len])
            for p in picked_up:
                cups.remove(p)

            self.destination_cup = self.current_cup - 1 or cups_len
            while self.destination_cup in picked_up:
                self.destination_cup = self.destination_cup - 1 or cups_len
            self.destination_cup_idx = cups.index(self.destination_cup)

            cups = cups[: self.destination_cup_idx + 1] + picked_up + cups[self.destination_cup_idx + 1:]
        ix_1 = cups.index(1)
        self.result = cups[ix_1 + 1:] + cups[:ix_1]
        self.result = ''.join(str(x) for x in self.result)


def prep(input,maximum):
    ring = [input[0]] + ([0] * len(input))
    for x in range(len(input)):
        ring[input[x]] = input[x+1] if x+1 < len(input) else max(input)+1
    for x in range(max(input)+1,maximum):
        ring.append(x+1)
    ring.append(ring[0])
    ring.append(maximum)
    ring.append(min(input))
    return ring


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [int(x) for x in file.read()]
    crabcups = CrabCups()
    crabcups.circle = input_file
    crabcups.rounds = 100
    crabcups.play_game()
    print(f'Part1: {crabcups.result}')
    print(prep(input_file, 10))
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
