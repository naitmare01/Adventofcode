#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
# from copy import deepcopy
import time
import re


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Calculator(int):
    def __init__(self, int):
        self.memory = []

    def __add__(self, other):
        return Calculator(int(self) + int(other))

    def __sub__(self, other):
        return Calculator(self * other)

    def calculate(self, expressions):
        self.memory.append(eval(
            re.sub(
                r"\d+",
                lambda match: f"Calculator({match.group(0)})",
                expressions.replace("*", "-"),
            )
        ))


class Calculator_pt2(int):
    def __init__(self, int):
        self.memory = []

    def __add__(self, other):
        return Calculator_pt2(int(self) * int(other))

    def __mul__(self, other):
        return Calculator_pt2(int(self) + int(other))

    def calculate(self, expressions):
        self.memory.append(eval(
            re.sub(
                r"\d+",
                lambda match: f"Calculator_pt2({match.group(0)})",
                expressions.replace("+", "x").replace("*", "+").replace("x", "*"),
            )
        ))


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()

    calc = Calculator(1)
    calc2 = Calculator_pt2(1)
    for row in input_file:
        row = str(row)
        calc.calculate(row)
        calc2.calculate(row)
    print(f'Part1: {sum(calc.memory)}')
    print(f'Part2: {sum(calc2.memory)}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
