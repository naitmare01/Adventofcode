#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import numpy as np
# import itertools


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class HolidayGrid():
    def __init__(self, grid_size):
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.number_of_lights = 0
        self.brightness = {}

    def control_lights(self, instructions):
        instructions = instructions.split()

        if 'toggle' in instructions:
            x_values = [int(x) for x in (instructions[1]).split(',')]
            y_values = [int(x) for x in (instructions[-1]).split(',')]
            all_x_values = np.arange(x_values[0], y_values[0] + 1).tolist()
            all_y_values = np.arange(x_values[1], y_values[1] + 1).tolist()

            for x in all_x_values:
                for y in all_y_values:
                    self.grid[x][y] = 1 - self.grid[x][y]
                    b_index = (list(zip([x], [y]))[0])
                    self.set_brightness(b_index, instructions[0])

        else:
            x_values = [int(x) for x in (instructions[2]).split(',')]
            y_values = [int(x) for x in (instructions[-1]).split(',')]
            all_x_values = np.arange(x_values[0], y_values[0] + 1).tolist()
            all_y_values = np.arange(x_values[1], y_values[1] + 1).tolist()

            if instructions[1] == 'on':
                new_value = 1
            elif instructions[1] == 'off':
                new_value = 0

            for x in all_x_values:
                for y in all_y_values:
                    self.grid[x][y] = new_value
                    b_index = (list(zip([x], [y]))[0])
                    self.set_brightness(b_index, instructions[1])

    def set_brightness(self, key, option):
        if key not in self.brightness:
            self.brightness[key] = 0

        if option == 'on':
            self.brightness[key] += 1
        elif option == 'off':
            if self.brightness[key] >= 1:
                self.brightness[key] -= 1
        elif option == 'toggle':
            self.brightness[key] += 2

    def count_number_of_lights(self):
        self.number_of_lights = (sum([sum(x) for x in self.grid]))


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    part1 = HolidayGrid(1000)
    for row in input_file:
        part1.control_lights(row)
    part1.count_number_of_lights()

    print("Part1:", part1.number_of_lights)
    print("Part2:", sum(part1.brightness.values()))


if __name__ == '__main__':
    main()
