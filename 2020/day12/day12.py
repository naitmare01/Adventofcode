#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Ship():
    def __init__(self):
        self.reset()

    def reset(self):
        self.angle = 90  # E
        self.angle_directions = {0: "N", 90: "E", 180: "S", 270: "W"}
        self.directions = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        self.position = {"x": 0, "y": 0}
        self.instructions = None

    def run_ship(self):
        for line in self.instructions:
            instruction = line[0]
            value = line[1]

            if instruction in self.directions:
                self.position["x"] += (value * self.directions[instruction][0])
                self.position["y"] += (value * self.directions[instruction][1])

            if instruction == "F":
                facing = (self.angle_directions[self.angle])
                self.position["x"] += (value * self.directions[facing][0])
                self.position["y"] += (value * self.directions[facing][1])

            if instruction in {"R", "L"}:
                self.angle += (value if instruction == 'R' else 360 - value)
                self.angle %= 360


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.splitlines()
        input_file = [(x[:1], int(x[1:])) for x in input_file]
    ship = Ship()
    ship.instructions = input_file
    ship.run_ship()
    print("Part1:", sum([abs(x) for x in ship.position.values()]))


if __name__ == '__main__':
    main()


# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.
