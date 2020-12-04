#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class PacketScanners: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    def __init__(self):
        self.severity = 0
        self.delay = 0

    def traverse_map(self, lengths):
        total = 0
        for key in lengths.keys():
            if key % (2 * (lengths[key] - 1)) == 0:
                total += lengths[key] * key
        self.severity = total

    def shortest_delay(self, lengths):
        def does_trigger(lengths, delay):
            for key in lengths.keys():
                if (key + delay) % (2 * (lengths[key] - 1)) == 0:
                    return True
            return False
        delay = 0
        while does_trigger(lengths, delay):
            delay += 1
        self.delay = delay

def main():
    args = arguments()

    with open(args.file) as inp:
        lengths = {}
        for line in inp:
            ind, length = map(int, line.strip().split(': '))
            lengths[ind] = length

    scanner = PacketScanners()
    scanner.traverse_map(lengths)
    print("Part1:", scanner.severity)
    scanner.shortest_delay(lengths)
    print("Part2:", scanner.delay)

if __name__ == '__main__':
    main()
