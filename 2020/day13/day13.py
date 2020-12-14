#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from functools import lru_cache
from copy import deepcopy
import time


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
        self.instructions = None
        self.timestamps = dict()
        self.depart = None
        self.earliest_bus = dict()
        self.earliest_subsequent_bus = None

    @lru_cache(maxsize=None)
    def find_subsequent_bus(self):
        self.instructions = self.instructions.pop()
        self.instructions = self.instructions.split(',')
        self.instructions = [int(x) if x != 'x' else x for x in self.instructions]
        idmap = {key: val for val, key in filter(lambda x: x[1] != 'x', enumerate(self.instructions))}
        idlist = [id for id in idmap]

        step = idlist[0]
        start = 0
        for id in idlist[1:]:
            delta = idmap[id]
            for i in range(start, step * id, step):
                if not (i + delta) % id:
                    step = step * id
                    start = i
        self.earliest_subsequent_bus = start

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
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.splitlines()
    timetable = TimeTable()
    timetable.instructions = deepcopy(input_file)
    timetable.find_earliest_bus()
    part1_answer = ([int(x) for x in timetable.earliest_bus.values()][0] - timetable.depart) * [int(x) for x in timetable.earliest_bus.keys()][0]
    print("Part1:", part1_answer)

    timetable.reset()
    timetable.instructions = deepcopy(input_file)
    timetable.find_subsequent_bus()
    print("Part2:", timetable.earliest_subsequent_bus)

    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))


if __name__ == '__main__':
    main()

# In the example, the first time Bus 7 (t offset = 0) and Bus 13 align (t offset = 1) , is t = 77. With the current increment being 7,
# the new increment is 7 * 13 = 91, meaning the current t of 77 + 91 is the next time the pattern will repeat. You keep incrementing with 91,
# until Bus 59 can be found (at t offset = 4, since we're skipping minutes 2 and 3). Rinse and repeat until you reach the end of your line.
