#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import collections


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Claim:  # pylint: disable=too-few-public-methods, too-many-instance-attributes
    def __init__(self):
        self.claim_id = None
        self.starting_x = None
        self.starting_y = None
        self.ending_x = None
        self.ending_y = None
        self.claim_area = None
        self.total_area = []

    def build_claim(self, claim):
        self.claim_id = claim.split()[0][1:]
        self.starting_x = int(claim.split()[2].split(',')[0])
        self.starting_y = int(claim.split()[2].split(',')[1][:-1])

        area_x = claim.split()[3].split('x')[0]
        area_y = claim.split()[3].split('x')[1]
        ending_x = self.starting_x + (int(area_x) - 1)
        ending_y = self.starting_y + (int(area_y) - 1)

        self.ending_x = ending_x
        self.ending_y = ending_y

        area = []
        for x_marker in range(self.starting_x, (self.ending_x + 1)):
            for y_marker in range(self.starting_y, (self.ending_y + 1)):
                area.append((x_marker, y_marker))
                self.total_area.append((x_marker, y_marker))

        self.claim_area = area


class MapMatrix:  # pylint: disable=too-few-public-methods
    def __init__(self):
        self.land = []

    def claim_land(self, cordinations):
        self.land.append(cordinations)


def find_overlapping_fabric(total_area):
    return [item for item, count in collections.Counter(total_area).items() if count > 1]


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().splitlines()

    part1_total_area = []
    all_claims = []
    for row in input_file:
        claim = Claim()
        all_claims.append(claim)
        claim.build_claim(row)
        part1_total_area.append(claim.total_area)

    flat_list_part1 = [item for sublist in part1_total_area for item in sublist]
    part1_result = find_overlapping_fabric(flat_list_part1)
    print("Part 1:", len(part1_result))

    map_of_claims = MapMatrix()
    for single_claim in all_claims:
        for cord in single_claim.claim_area:
            map_of_claims.claim_land(cord)
    print(map_of_claims.land)


if __name__ == '__main__':
    main()
