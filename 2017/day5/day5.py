#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Maze: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self, instructions):
        self.steps_to_exit_part1 = 0
        self.steps_to_exit_part2 = 0
        self.instructions = instructions.copy()

    def exit_maze_part1(self):
        index = 0
        while True:
            if index >= len(self.instructions):
                break
            instruction = self.instructions[index]
            self.instructions[index] = self.instructions[index] + 1 #update the place we visited
            index = instruction + index
            self.steps_to_exit_part1 = self.steps_to_exit_part1 + 1

    def exit_maze_part2(self):
        index = 0
        while True:
            if index >= len(self.instructions):
                break
            instruction = self.instructions[index]

            if instruction >= 3:
                self.instructions[index] = self.instructions[index] - 1 #update the place we visited
            else:
                self.instructions[index] = self.instructions[index] + 1 #update the place we visited
            index = instruction + index
            self.steps_to_exit_part2 = self.steps_to_exit_part2 + 1

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().split("\n")
        input_file = [int(x) for x in input_file]

    maze = Maze(input_file)
    maze.exit_maze_part1()
    print("part1:", maze.steps_to_exit_part1)

    maze = Maze(input_file)
    maze.exit_maze_part2()
    print("part2:", maze.steps_to_exit_part2)

if __name__ == '__main__':
    main()
