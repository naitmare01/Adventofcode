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


class Computer:
    '''Computer'''
    def __init__(self):
        self.cycles = 0
        self.register = {"x": 1}
        self.history = {}
        self.signal_strengths = []
        self.crt = ["." for i in range(240)]
        self.crt_pos = 0
        self.crt_row = 0

    def process(self, instruction):
        '''process'''
        if instruction == "noop":
            self.cycles += 1
            self.draw_crt()
            self.history[self.cycles] = self.register["x"]
        if instruction.startswith("addx"):
            self.addx_cycle(instruction)

    def addx_cycle(self,instruction):
        '''Addx'''
        for i in range(2):
            self.cycles += 1
            self.draw_crt()
            if i == 0:
                self.history[self.cycles] = self.register["x"]
            else:
                self.history[self.cycles] = self.register["x"]
        self.register["x"] += int(instruction.split()[-1])

    def draw_crt(self):
        '''Draw Crt'''
        neighbors = self.register["x"] + 1, self.register["x"] - 1, self.register["x"]
        if self.crt_pos in neighbors:
            self.crt[(self.crt_pos + self.crt_row * 40)] = "#"

        self.crt_pos += 1
        if self.crt_pos % 40 == 0:
            self.crt_pos = 0
            self.crt_row += 1

    def calculate_signal_strength(self, cycles):
        '''Calc pt1'''
        for cycle in cycles:
            result = {value for (key,value) in self.history.items() if key == cycle}
            result = int(str(result).replace('{', '').replace('}', ''))
            result = result * cycle
            self.signal_strengths.append(result)



def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
    comp = Computer()
    for row in input_file:
        comp.process(row)
    comp.calculate_signal_strength([20, 60, 100, 140, 180, 220])
    result_pt1 = sum(comp.signal_strengths)
    print("Part1:", result_pt1)
    print("Part2:")
    crt_rows_display = comp.crt[:40], comp.crt[40:80], comp.crt[80:120], comp.crt[120:160], comp.crt[160:200], comp.crt[200:240]
    for row in crt_rows_display:
        print(" ".join(row))

if __name__ == '__main__':
    main()
