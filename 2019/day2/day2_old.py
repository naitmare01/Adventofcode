#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

def compute_intcode(input_arr):
    input_arr = input_arr[:]
    for index in range(0, len(input_arr), 4):

        operator = input_arr[index]

        if operator == 99: #Halting
            return input_arr[0]

        number_a = input_arr[input_arr[index + 1]]
        number_b = input_arr[input_arr[index + 2]]

        if operator == 1: #Addition
            input_arr[input_arr[index + 3]] = number_a + number_b
        elif operator == 2: #Multiplication
            input_arr[input_arr[index + 3]] = number_a * number_b

    return input_arr[0]

def determine_what_pair_inputs(input_file, noun_verb_range, wanted):
    for noun in range(noun_verb_range):
        for verb in range(noun_verb_range):
            input_file = list(input_file)
            input_file[1] = noun
            input_file[2] = verb

            output = compute_intcode(input_file)

            if output == wanted:
                return 100 * noun + verb
    return False

def main():
    args = arguments()

    with open(args.file) as file:
        file = list(file.read().split(','))
        input_file = map(int, file)
        part1_result = compute_intcode(input_file)
        part2_result = determine_what_pair_inputs(input_file, 100, 19690720)

    print("Part 1:", part1_result)
    print("Part 2:", part2_result)


if __name__ == '__main__':
    main()
