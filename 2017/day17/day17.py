#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Spinlock: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    def __init__(self, number_of_steps, number_of_insertions):
        self.number_of_steps = number_of_steps
        self.number_of_insertions = number_of_insertions
        self.spinlock = [0]
        self.part1_result = 0
        self.part2_result = 0

    def insert_numbers(self):
        current_index = 0
        for step in range(0, self.number_of_insertions):
            if self.number_of_steps % (step + 1) == 0:
                current_index = current_index + 1
            else:
                new_index = self.number_of_steps % (step + 1) + current_index
                if new_index > (len(self.spinlock) - 1):
                    current_index = new_index - (len(self.spinlock) - 1)
                else:
                    current_index = new_index + 1
            self.spinlock.insert(current_index, (step + 1))
        self.part1_result = self.spinlock[(self.spinlock.index(self.number_of_insertions) + 1)]

    def insert_numbers_part2(self):
        current_index = 0
        for step in range(1, self.number_of_insertions):
            current_index = (current_index + self.number_of_steps) % step
            if current_index == 0:
                self.part2_result = step
            current_index = current_index + 1

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = int(file.read().strip())

    spinlock = Spinlock(input_file, 2017)
    spinlock.insert_numbers()
    print("Part1:", spinlock.part1_result)

    spinlock2 = Spinlock(input_file, 50000001)
    spinlock2.insert_numbers_part2()
    print("Part2:", spinlock2.part2_result)


if __name__ == '__main__':
    main()
