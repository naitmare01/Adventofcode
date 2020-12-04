#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import itertools


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Ingredients():
    def __init__(self):
        self.name = None
        self.capacity = None
        self.durability = None
        self.flavor = None
        self.texture = None
        self.calories = None


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    all_permutations = itertools.permutations([x for x in range(101)], len(input_file))
    print(set(all_permutations))

    for row in input_file:
        ingredients = Ingredients()
        ingredients.name = row.split()[0]
        ingredients.capacity = row.split()[2]
        ingredients.durability = row.split()[4]
        ingredients.flavor = row.split()[4]
        ingredients.texture = row.split()[6]
        ingredients.calories = row.split()[8]
        print(ingredients.__dict__)


if __name__ == '__main__':
    main()
