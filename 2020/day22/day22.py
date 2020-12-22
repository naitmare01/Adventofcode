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


class CrabCombat():
    def __init__(self):
        self.reset()

    def reset(self):
        self.instructions = None
        self.player1 = []
        self.player2 = []
        self.last_winner = []
        self.winning_score = 0

    def setup_game(self):
        self.player1 = ([int(x) for x in self.instructions[0] if x.isdigit()])
        self.player2 = ([int(x) for x in self.instructions[1] if x.isdigit()])

    def play_game(self):
        while True:
            if len(self.player1) == 0 or len(self.player2) == 0:
                break
            elif self.player1[0] > self.player2[0]:
                self.player1.append(self.player1[0])
                self.player1.append(self.player2[0])
                self.player1.pop(0)
                self.player2.pop(0)
                self.last_winner = self.player1
            else:
                self.player2.append(self.player2[0])
                self.player2.append(self.player1[0])
                self.player1.pop(0)
                self.player2.pop(0)
                self.last_winner = self.player2
        self.winning_score = (sum([(i * (idx + 1)) for idx, i in enumerate(reversed(self.last_winner))]))


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [x.splitlines() for x in file.read().split('\n\n')]
    crabcombat = CrabCombat()
    crabcombat.instructions = input_file
    crabcombat.setup_game()
    crabcombat.play_game()
    print(f'Part1: {crabcombat.winning_score}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
