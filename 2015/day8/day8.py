#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import codecs

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Matchsticks:
    def __init__(self, whole_string):
        self.whole_string = whole_string
        self.converted_string = None
        self.length_whole_string = None
        self.length_converted_string = None

    def calc_length_whole_string(self):
        self.length_whole_string = len(self.whole_string)

    def calc_length_converted_string(self):
        escaped_str = self.whole_string
        escaped_str = escaped_str[1:]
        escaped_str = escaped_str[:-1]
        self.converted_string = codecs.getdecoder("unicode_escape")(escaped_str)[0]
        self.length_converted_string = len(self.converted_string)


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    result = []
    for row in input_file:
        part1 = Matchsticks(row)
        part1.calc_length_whole_string()
        part1.calc_length_converted_string()
        result.append(part1)

    print("Part1:", (sum([x.length_whole_string for x in result])) - (sum([x.length_converted_string for x in result])))
    print("Part2:", sum(2+s.count('\\')+s.count('"') for s in open('input')))

if __name__ == '__main__':
    main()
