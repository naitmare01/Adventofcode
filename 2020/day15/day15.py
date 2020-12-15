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

    def reset(self):
        self.instructions = None
        self.spoken_numbers = []

    def play_game(self):
        for idx, num in enumerate(self.instructions):
            self.spoken_numbers.append((idx + 1, num))
        turn = len(self.instructions)
        while turn < 2020:
            turn += 1
            last_number_spoken = self.spoken_numbers[-1][-1]
            times_last_number_spoken = len([x[1] for x in self.spoken_numbers if x[1] == last_number_spoken])

            if times_last_number_spoken == 1:
                value = 0
            else:
                all_times_spoken = [x for x in self.spoken_numbers if x[1] == last_number_spoken]
                last_index = all_times_spoken.pop()
                second_to_last = all_times_spoken.pop()
                value = last_index[0] - second_to_last[0]
            self.spoken_numbers.append((turn, value))
        


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.split(',')
        input_file = [int(x) for x in input_file]

    game = MemoryGame()
    game.instructions = input_file
    game.play_game()
    print("Part1:", game.spoken_numbers[-1][-1])
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))


if __name__ == '__main__':
    main()
