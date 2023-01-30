#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

def arguments():
    '''args'''
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

# int: number of lines to light up
NUMBER_OF_LINES = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

class Decoder:
    '''Decoder'''
    def __init__(self):
        self.instruction = None
        self.digit = None
        self.number_output_values = 0

    def find_digits(self, digit):
        '''Find digits'''
        for row in self.instruction:
            words = row[1].split()
            word_len = [NUMBER_OF_LINES[x] for x in digit]
            self.number_output_values += (len(self.intersection([len(x) for x in words], word_len)))

    def intersection(self, lst1, lst2):
        '''Intersection'''
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        return lst3


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.split('\n')
        input_file = [x.split(' | ') for x in input_file]
    decoder = Decoder()
    decoder.instruction = input_file
    part1_digits = [1, 4, 7, 8]
    decoder.find_digits(part1_digits)
    print("Part1:", decoder.number_output_values)

if __name__ == '__main__':
    main()
