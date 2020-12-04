#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Reindeer:
    def __init__(self):
        self.name = None
        self.speed = None
        self.time_in_the_air = None
        self.resting_time = None
        self.distance = None
        self.racing_time = None

    def calculate_distance(self):
        timespan = self.time_in_the_air + self.resting_time
        cycles = self.racing_time / timespan

        self.distance = int(cycles) * self.speed * 10


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    for row in input_file:
        deer_split = (row.split())
        reindeer = Reindeer()
        reindeer.name = deer_split[0]
        reindeer.speed = int(deer_split[3])
        reindeer.time_in_the_air = int(deer_split[6])
        reindeer.resting_time = int(deer_split[13])
        reindeer.racing_time = 10
        reindeer.calculate_distance()
        print(reindeer.__dict__)


if __name__ == '__main__':
    main()
