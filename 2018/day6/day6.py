#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class StarMap: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    def __init__(self):
        self.map = None
        self.starting_cord = None
        self.ending_cord = None

    def draw_map(self, cords):
        self.starting_cord = int(cords[0])
        self.ending_cord = cords[-1]
        print(self.starting_cord[0], self.starting_cord[1])
        #for x_cord in range(self.starting_cord[0], (self.ending_cord[0]) + 1):
        #    for y_cord in range(self.starting_cord[1], (self.ending_cord[1] + 1)):
        #        print(x_cord, y_cord)

def main():
    args = arguments()
    work_list = []

    with open(args.file) as file:
        input_file = file.read().strip().splitlines()
        for row in input_file:
            row = row.split(',')
            row = (int(num) for num in row)
            work_list.append(tuple(row))

    work_list = sorted(work_list)
    print(work_list)
    star_map = StarMap()
    star_map.draw_map(input_file)
    #print(star_map.starting_cord, star_map.ending_cord)

if __name__ == '__main__':
    main()
