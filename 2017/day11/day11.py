#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class HexEd: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self, steps):
        self.steps = steps
        self.map = [(0, 0, 0)]
        self.manhattan_distance = None
        self.end_cords = None
        self.furthest_distance = None

    def traverse_grid(self):
        for idx, direction in enumerate(self.steps):
            if direction == "ne":
                new_x = self.map[idx][0] + 1
                new_y = self.map[idx][1]
                new_z = self.map[idx][2] - 1
            elif direction == "n":
                new_x = self.map[idx][0]
                new_y = self.map[idx][1] + 1
                new_z = self.map[idx][2] - 1
            elif direction == "nw":
                new_x = self.map[idx][0] - 1
                new_y = self.map[idx][1] + 1
                new_z = self.map[idx][2]
            elif direction == "sw":
                new_x = self.map[idx][0] - 1
                new_y = self.map[idx][1]
                new_z = self.map[idx][2] + 1
            elif direction == "s":
                new_x = self.map[idx][0]
                new_y = self.map[idx][1] - 1
                new_z = self.map[idx][2] + 1
            elif direction == "se":
                new_x = self.map[idx][0] + 1
                new_y = self.map[idx][1] - 1
                new_z = self.map[idx][2]

            self.map.append((new_x, new_y, new_z))
        self.end_cords = self.map[-1]

    def calculate_manhattan_distance(self):
        self.manhattan_distance = (abs(self.map[0][0] - self.end_cords[0]) + abs(self.map[0][1] - self.end_cords[1]) + abs(self.map[0][2] - self.end_cords[2])) / 2

    def calculate_furtest_distance(self):
        result = []
        for cord in self.map:
            result.append((abs(self.map[0][0] - cord[0]) + abs(self.map[0][1] - cord[1]) + abs(self.map[0][2] - cord[2])) / 2)
        self.furthest_distance = max(result)



def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().split(",")

    hex_grid = HexEd(input_file)
    hex_grid.traverse_grid()
    hex_grid.calculate_manhattan_distance()
    print("part1:", int(hex_grid.manhattan_distance))
    hex_grid.calculate_furtest_distance()
    print("part2:", int(hex_grid.furthest_distance))

if __name__ == '__main__':
    main()
