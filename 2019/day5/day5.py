#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Instruction:
    def __init__(self, operator):
        self.operator = operator
        self.operation = None
        self.input_one = None
        self.input_two = None
        self.result = None
        self.modes = None

    def define_operation(self):
        if self.operator == 1:
            self.operation = "ADDITION"
        if self.operator == 2:
            self.operation = "MULTIPLICATION"
        if self.operator == 3:
            self.operation = "INPUT"
        if self.operator == 4:
            self.operation = "OUTPUT"
        if self.operator == 99:
            self.operation = "TERMINATION"

    def get_modes(self, intcode):
        self.modes = intcode

    def get_inputs(self, intcode, index):
        self.input_one = intcode[intcode[index + 1]]
        self.input_two = intcode[intcode[index + 2]]

    def get_result(self, intcode):
        self.result = intcode[0]


def compute_intcode(input_arr):
    for index in range(0, len(input_arr), 4):
        instructions = Instruction(input_arr[index])
        instructions.define_operation()
        print(instructions.operator)

        if instructions.operation == "TERMINATION":
            instructions.get_result(input_arr)
            return instructions.result

        #instructions.get_inputs(input_arr, index) # Get inputs from [1] and [2]

        if instructions.operation == "ADDITION":
            #input_arr[input_arr[index + 3]] = instructions.input_one + instructions.input_two
            print("op: 1")
        elif instructions.operation == "MULTIPLICATION":
            #input_arr[input_arr[index + 3]] = instructions.input_one * instructions.input_two
            print("op: 2")
        elif instructions.operation == "INPUT":
            print("op: 3")
        elif instructions.operation == "OUTPUT":
            print("op: 4")

    instructions.get_result(input_arr)
    return instructions.result

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


    print("Part 1:", part1_result)
    #print("Part 2:", part2_result)

if __name__ == '__main__':
    main()
