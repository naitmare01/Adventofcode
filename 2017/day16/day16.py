#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from string import ascii_lowercase

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class PermutationPromenade: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    def __init__(self):
        self.programs = list(ascii_lowercase[:16])
        self.programs_org = list(ascii_lowercase[:16])
        self.instructions = None
        self.ordered_program = ""
        self.cycles = 0

    def dance(self, iterations):
        for ite in range(0, iterations):
            if self.cycles == 0:
                for instruction in self.instructions:
                    if instruction[0] == "s":
                        number_of_spins = int(instruction[1:])
                        for spins in range(0, number_of_spins):
                            self.programs.insert(0, self.programs[-1])
                            self.programs.pop()
                    elif instruction[0] == "x":
                        exchange_partners = instruction[1:].split("/")
                        exchange_partners = [int(x) for x in exchange_partners]
                        partner0 = self.programs[exchange_partners[0]]
                        partner1 = self.programs[exchange_partners[1]]
                        self.programs[exchange_partners[0]] = partner1
                        self.programs[exchange_partners[1]] = partner0
                    elif instruction[0] == "p":
                        partners = instruction[1:].split("/")
                        partner0_index = self.programs.index(partners[0])
                        partner1_index = self.programs.index(partners[1])
                        self.programs[partner0_index] = partners[1]
                        self.programs[partner1_index] = partners[0]

                    if self.programs == self.programs_org:
                        print(ite, self.programs, self.programs_org)
                        self.cycles = ite
                self.ordered_program = ",".join([x for x in self.programs]).replace(",", "")
            else:
                self.ordered_program = ",".join([x for x in self.programs]).replace(",", "")
                break

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().split(",")

    promenade = PermutationPromenade()
    promenade.instructions = input_file
    promenade.dance(1)
    print("Part1:", promenade.ordered_program)

    #part2
    promenade = PermutationPromenade()
    promenade.instructions = input_file
    #promenade.dance(1000000000)
    #num = 1000000000 % promenade.cycles
    promenade.dance(32)
    print("Part2:", promenade.ordered_program, promenade.cycles)

if __name__ == '__main__':
    main()
