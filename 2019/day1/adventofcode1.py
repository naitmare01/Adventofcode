#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Checks running version of net equipment in LibreNMS and looks for CVE-vurnabilites.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

def get_fuel_requirement_fuel(fuel):
    fuel_requirement = 0
    more_fuel = True
    while more_fuel is True:
        adding_fuel = int(float(fuel / 3) - 2)
        if adding_fuel <= 0:
            more_fuel = False
            break
        fuel_requirement = fuel_requirement + adding_fuel
        fuel = adding_fuel

    return fuel_requirement

def get_mass(module_mass):
    result = int(module_mass / 3) - 2
    result = result + get_fuel_requirement_fuel(result)
    return result

def main():
    args = arguments()
    sum_of_mass = 0

    with open(args.file) as input_file:
        for line in input_file:
            sum_of_mass = sum_of_mass + (get_mass(float(line)))
            if 'str' in line:
                break

    print(sum_of_mass)

if __name__ == '__main__':
    main()
