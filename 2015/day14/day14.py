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
        self.active_time = None
        self.resting_time = None
        self.distance_per_cycle = None
        self.cycle_length = None
        self.result = None

    def calculate_distance(self, time):
        self.distance_per_cycle = self.active_time * self.speed
        self.cycle_length = self.active_time + self.resting_time

        full_cycles = int(time / self.cycle_length)
        remaninder = time % self.cycle_length

        if remaninder >= self.active_time:
            self.result = (full_cycles + 1) * self.distance_per_cycle
        else:
            self.result = full_cycles * self.distance_per_cycle + remaninder * self.speed


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    deers = []
    for row in input_file:
        deer_data = row.split()
        deer = Reindeer()
        deer.name = deer_data[0]
        deer.speed = int(deer_data[3])
        deer.active_time = int(deer_data[6])
        deer.resting_time = int(deer_data[13])
        deer.calculate_distance(2503)
        deers.append(deer)

    print(max([x.result for x in deers]))


if __name__ == '__main__':
    main()
