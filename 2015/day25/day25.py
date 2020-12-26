#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from copy import deepcopy


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class EncryptionMachine():
    def __init__(self):
        self.reset()

    def reset(self):
        self.first_code = 20151125
        self.code_coords = (2947, 3029)
        self.result = None
        return

    def next_code(self, cur_code):
        return (cur_code * 252533) % 33554393

    def get_code_count(self, row, column):
        return sum(range(row + column - 1)) + column

    def run_program(self):
        code_count = self.get_code_count(*self.code_coords)
        cur_code = self.first_code
        for i in range(code_count - 1):
            cur_code = self.next_code(cur_code)
        self.result = cur_code


def main():
    input_file = (2947, 3029)
    enc = EncryptionMachine()
    enc.code_coords = input_file
    enc.run_program()
    print(enc.result)


if __name__ == '__main__':
    main()
