#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import re

def arguments():
    '''args'''
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
    numbers = [re.findall('[0-9]+', x) for x in input_file]
    day1 =  [int("".join((x[0][0], x[-1][-1]))) for x in numbers]
    print(sum(day1))

if __name__ == '__main__':
    main()

