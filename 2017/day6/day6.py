#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class MemoryReallocation: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self):
        self.infinite_redistribution_count = 0
        self.index_of_duplicates = None
        self.loop_size = None

    def debugger(self, banks):
        result = []
        while True:
            index = banks.index(max(banks))
            redist_value = banks[index]
            banks[index] = 0
            index_value_loop = index + 1

            for num in range(redist_value):
                if index_value_loop > (len(banks) - 1):
                    index_value_loop = 0

                banks[index_value_loop] = banks[index_value_loop] + 1

                if index_value_loop >= (len(banks) - 1):
                    index_value_loop = 0
                else:
                    index_value_loop = index_value_loop + 1

            if result.count(banks) == 0:
                result.append([a for a in banks])
            else:
                result.append([a for a in banks])
                break
        self.infinite_redistribution_count = len(result)
        self.index_of_duplicates = ([i for i in range(len(result)) if result[i] == result[-1]])
        self.loop_size = self.infinite_redistribution_count - 1 - self.index_of_duplicates[0]


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().split("\t")
        input_file = [int(x) for x in input_file]

    memory_reallocation = MemoryReallocation()
    memory_reallocation.debugger(input_file)
    print("part1:", memory_reallocation.infinite_redistribution_count)
    print("part2:", memory_reallocation.loop_size)

if __name__ == '__main__':
    main()
