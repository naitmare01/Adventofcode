#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class TimeTable():
    def __init__(self):
        self.reset()

    def reset(self):
        self.time = None
        self.instructions = None
        self.timestamps = dict()
        self.depart = None
        self.earliest_bus = dict()

    def find_earliest_bus(self):
        self.depart = int(self.instructions[0])
        self.instructions = self.instructions.pop()
        self.instructions = self.instructions.split(',')
        self.instructions = {x for x in self.instructions if x.isdigit()}
        for bus in self.instructions:
            if self.depart % int(bus) == 0:
                self.timestamps[bus] = (self.depart)
            else:
                iterations = 1
                while True:
                    if (self.depart + iterations) % int(bus) == 0:
                        self.timestamps[bus] = (self.depart + iterations)
                        break
                    else:
                        iterations += 1
        self.earliest_bus[min(self.timestamps, key=self.timestamps.get)] = self.timestamps[min(self.timestamps, key=self.timestamps.get)]


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.splitlines()
    timetable = TimeTable()
    timetable.instructions = input_file
    timetable.find_earliest_bus()
    part1_answer = ([int(x) for x in timetable.earliest_bus.values()][0] - timetable.depart) * [int(x) for x in timetable.earliest_bus.keys()][0]
    print("Part1:", part1_answer)
    print(timetable.__dict__)


if __name__ == '__main__':
    main()
