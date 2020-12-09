#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import itertools


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Player():
    def __init__(self):
        self.reset()
        self.min_total_cost_for_win = set()
        self.max_total_cost_for_lose = set()

    def reset(self):
        self.hp = 100
        self.total_dmg = 0
        self.total_armor = 0

    def attack(self, opponent):
        dealt_dmg = self.total_dmg - opponent.total_armor
        if dealt_dmg <= 0:
            dealt_dmg = 1
        return dealt_dmg

    def figth(self, opponent):
        # Cost  Damage  Armor
        weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
        armor = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
        rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

        for wep in weapons:
            for arm in armor:
                for r1, r2 in itertools.combinations(rings, 2):
                    self.reset()
                    opponent.reset()
                    self.total_armor = sum([arm[2], r1[2], r2[2]])
                    self.total_dmg = sum([wep[1], r1[1], r2[1]])

                    while True:
                        opponent.hp -= self.attack(opponent)
                        if opponent.hp <= 0:
                            self.min_total_cost_for_win.add(sum([wep[0], arm[0], r1[0], r2[0]]))
                            break
                        self.hp -= opponent.attack(self)
                        if self.hp <= 0:
                            self.max_total_cost_for_lose.add(sum([wep[0], arm[0], r1[0], r2[0]]))
                            break


class Boss():
    def __init__(self):
        self.reset()

    def reset(self):
        self.hp = 100
        self.total_dmg = 8
        self.total_armor = 2

    def attack(self, opponent):
        dealt_dmg = self.total_dmg - opponent.total_armor
        if dealt_dmg <= 0:
            dealt_dmg = 1
        return dealt_dmg


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = [line.strip() for line in file.readlines()]
        input_file = [x.split(': ') for x in input_file]

    player = Player()
    boss = Boss()

    player.hp = 100
    player.total_dmg = 0
    player.total_armor = 0
    boss.hp = int(input_file[0][1])
    boss.total_armor = int(input_file[2][1])
    boss.total_dmg = int(input_file[1][1])
    player.figth(boss)
    print("Part1:", min(player.min_total_cost_for_win))
    print("Part2:", max(player.max_total_cost_for_lose))


if __name__ == '__main__':
    main()
