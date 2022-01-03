#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class BianryDiagnostic:
    def __init__(self):
        self.reset()

    def reset(self):
        self.result = None


def find_gamma_rate(binary_list, epsilon):
    rate = ""
    for row in binary_list:
        num_of_ones = sum([int(x) for x in row])
        num_of_zeros = len(row) - num_of_ones
        if epsilon:
            if num_of_ones > num_of_zeros:
                rate += "0"
            else:
                rate += "1"
        else:
            if num_of_ones > num_of_zeros:
                rate += "1"
            else:
                rate += "0"
    return rate


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = [[y for y in x] for x in input_file]

    rotated = zip(*input_file[::-1])
    gamma_rate = find_gamma_rate(rotated, False)
    rotated = zip(*input_file[::-1])
    epsilon_rate = find_gamma_rate(rotated, True)
    result_part1= (int(gamma_rate, 2)) * (int(epsilon_rate, 2))
    print("Part1:", result_part1)


if __name__ == '__main__':
    main()
