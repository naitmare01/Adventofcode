#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class CorruptionChecksum: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self):
        self.checksum = 0
        self.checksum_part2 = 0

    def calculate_checksum_part1(self, numbers):
        for row in numbers:
            self.checksum = self.checksum + (max(row) - min(row))

    def calculate_checksum_part2(self, numbers):
        for row in numbers:
            for index, number in enumerate(row):
                for idx, num in enumerate(row):
                    if idx == index:
                        continue
                    else:
                        if number % num == 0:
                            self.checksum_part2 = self.checksum_part2 + int((number / num))

def main():
    args = arguments()
    work_list = []

    with open(args.file) as file:
        input_file = file.read().strip("\t").split("\n")

    for row in input_file:
        row = row.replace(" ", ",")
        row = row.replace("\t", ",")
        row = row.split(",")
        row = [int(x) for x in row]
        work_list.append(row)

    corruption_checksum = CorruptionChecksum()
    corruption_checksum.calculate_checksum_part1(work_list)
    corruption_checksum.calculate_checksum_part2(work_list)
    print("part1:", corruption_checksum.checksum)
    print("part2:", corruption_checksum.checksum_part2)

if __name__ == '__main__':
    main()
