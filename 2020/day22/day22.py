#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
from copy import deepcopy
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
        self.instructions = None

    def reset(self):
        self.player1 = []
        self.player2 = []
        self.player1_history = []
        self.player2_history = []
        self.last_winner = []
        self.winning_score = 0

    def setup_game(self):
        self.player1 = ([int(x) for x in self.instructions[0] if x.isdigit()])
        self.player2 = ([int(x) for x in self.instructions[1] if x.isdigit()])

    def play_game(self, part):
        game = 1
        turn = 0
        while True:
            turn += 1
            if len(self.player1) == 0 or len(self.player2) == 0:
                break
            elif self.player1[0] > self.player2[0]:
                first = self.player1
                second = self.player2
            else:
                first = self.player2
                second = self.player1
            if part == 2:
                previous_p1 = [x for x in self.player1_history if self.player1 in x]
                previous_p2 = [x for x in self.player2_history if self.player2 in x]
                if len(previous_p1) != 0 or len(previous_p2) != 0:
                    self.last_winner = self.player1
                    break
                else:
                    self.player1_history.append(((game, turn), deepcopy(self.player1)))
                    self.player2_history.append(((game, turn), deepcopy(self.player2)))

                same_ammount_left_p1 = bool(first[0] <= len(first) - 1)
                same_ammount_left_p2 = bool(second[0] <= len(second) - 1)
                if same_ammount_left_p1 and same_ammount_left_p2:
                    print("New subgame")
            else:
                first.append(first[0])
                first.append(second[0])
                first.pop(0)
                second.pop(0)
                self.last_winner = first
        # if part == 2:
            # print("Player1", self.player1_history)
            # print("Player2", self.player2_history)
        self.winning_score = (sum([(i * (idx + 1)) for idx, i in enumerate(reversed(self.last_winner))]))


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [x.splitlines() for x in file.read().split('\n\n')]
    crabcombat = CrabCombat()
    crabcombat.instructions = input_file
    crabcombat.setup_game()
    crabcombat.play_game(1)
    print(f'Part1: {crabcombat.winning_score}')
    crabcombat.reset()
    crabcombat.setup_game()
    crabcombat.play_game(2)
    print(f'Part2: {crabcombat.winning_score}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
