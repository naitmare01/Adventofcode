#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import math


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class TobogganTrajectory():
    def __init__(self):
        self.map = None
        self.visited_locations = []
        self.number_of_trees = []

    def traverse_map(self, starting_x, starting_y):
        max_index = len(self.map[0]) - 1
        self.visited_locations = []
        inc_y = starting_y
        inc_x = starting_x
        while starting_y <= (len(self.map) - 1):
            self.visited_locations.append(self.map[starting_y][starting_x])

            if (starting_x + inc_x) > max_index:
                starting_x = starting_x + (inc_x - 1) - max_index
            else:
                starting_x += inc_x
            starting_y += inc_y
        self.number_of_trees.append(len([x for x in self.visited_locations if x == '#']))


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
    starting_map = []
    for row in input_file:
        starting_map.append([x for x in row])
    map_of_tree = TobogganTrajectory()
    map_of_tree.map = starting_map
    map_of_tree.traverse_map(3, 1)
    print("Part1:", map_of_tree.number_of_trees[0])

    # Part2
    map_of_tree.traverse_map(1, 1)
    map_of_tree.traverse_map(5, 1)
    map_of_tree.traverse_map(7, 1)
    map_of_tree.traverse_map(1, 2)
    print("Part2:", math.prod(map_of_tree.number_of_trees))


if __name__ == '__main__':
    main()
