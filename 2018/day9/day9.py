#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class MarbleMania():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.node_map = {}
        self.num_players = None
        self.last_marble = None
        self.player_score = dict()

    def setup_cirlce(self):
        node = Node(0)
        node.right = node
        node.left = node
        self.node_map[0] = node

    def score_points(self, player, point):
        if self.player_score.get(player):
            self.player_score[player] += point
        else:
            self.player_score[player] = point

    def play_game(self):
        current_node = self.node_map[0]
        idx = 1
        while True:
            for player in range(self.num_players):
                if idx % 23 != 0:
                    new_current = Node(idx)
                    node_before = current_node.right
                    node_after = current_node.right.right
                    new_current.right = node_after
                    new_current.left = node_before
                    node_after.left = new_current
                    node_before.right = new_current
                elif idx % 23 == 0:
                    self.score_points((player + 1), idx)
                    marble_to_remove = new_current.left.left.left.left.left.left.left
                    self.score_points((player + 1), marble_to_remove.value)
                    new_current = marble_to_remove.right
                    new_current.left = marble_to_remove.left
                    new_current.left.right = new_current
                    del self.node_map[marble_to_remove.value]

                self.node_map[new_current.value] = new_current
                current_node = new_current

                if idx == self.last_marble:
                    return
                else:
                    idx += 1


class Node():
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().split()
    # : high score is 8317 for test
    marble = MarbleMania()
    marble.num_players = int(input_file[0])
    marble.last_marble = int(input_file[6])
    marble.setup_cirlce()
    marble.play_game()
    print(f'Part1: {max(marble.player_score.values())}')
    # for k, v in marble.node_map.items():
    #    print("Left", v.left.value, "middle", k, "Right", v.right.value)
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
