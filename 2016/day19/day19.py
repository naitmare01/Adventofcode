#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Elf():
    def __init__(self):
        self.Id = None


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
    list_of_elves = [x for x in range(int(input_file))]
    list_of_elves = [1] * (len(list_of_elves))

    current_index = 0
    while True:
        if len([x for x in list_of_elves if x != 0]) == 1:
            break
        if current_index > (len(list_of_elves) - 1):
            current_index = 0
        if list_of_elves[current_index] == 0:
            current_index += 1
            continue
        indexes = [i for i, x in enumerate(list_of_elves) if x >= 1 and i != current_index]

        if len(indexes) >= 1:
            absolute_difference_function = lambda list_value: abs(list_value - current_index)
            closest_value = min(indexes, key=absolute_difference_function)
            list_of_elves[current_index] += list_of_elves[closest_value]
            list_of_elves[closest_value] = 0
        current_index += 1
        print(list_of_elves)


if __name__ == '__main__':
    main()
