#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import re
import numpy

def arguments():
    '''args'''
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Calculator:
    '''Calculator'''
    def __init__(self):
        self.instruction = None
        self.snafu_to_decimal = None

    def calculate_snafu_to_decimal(self):
        '''Calc'''
        total_sum = 0
        for idx, row in enumerate(self.instruction):
            row_sum = []
            for idx, char in enumerate(row):
                if idx == 0:
                    multiple_value = 1
                else:
                    multiple_value = 5 ** idx
                if char.isdigit():
                    char_multiplier = char
                else:
                    if char == "-":
                        char_multiplier = -1
                    else:
                        char_multiplier = -2
                row_sum.append((int(char_multiplier) * multiple_value))
            total_sum += (sum(row_sum))
        self.snafu_to_decimal = total_sum


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.split()
        input_file = [list(x[::-1]) for x in input_file]
    calc = Calculator()
    calc.instruction = input_file
    calc.calculate_snafu_to_decimal()
    print(calc.snafu_to_decimal)


if __name__ == '__main__':
    main()
