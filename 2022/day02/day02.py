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

def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    strategy_pt_2 = {
        'A X': 'A Z',
        'A Y': 'A X',
        'A Z': 'A Y',
        'B X': 'B X',
        'B Y': 'B Y',
        'B Z': 'B Z',
        'C X': 'C Y',
        'C Y': 'C Z',
        'C Z': 'C X'
    }

    response = {
        "X": 1,    # Rock
        "Y": 2,    # Paper
        "Z": 3     # Scissor
    }

    result = {
        'A X': 3, # Rock Rock
        'A Y': 6, # Rock Paper
        'A Z': 0, # Rock Scissor
        'B X': 0, # Paper Rock
        'B Y': 3, # Paper Paper
        'B Z': 6, # Paper Scissor
        'C X': 6, # Scissor Rock
        'C Y': 0, # Scissor Paper
        'C Z': 3, # Scissor Scissor
    }

    result_match = [result[x] for x in input_file]
    result_choice = ([response[x[-1]] for x in input_file])
    result_pt1 = sum(result_match) + sum(result_choice)

    print("Part1:", result_pt1)

    result_match_pt2 = ([result[(strategy_pt_2[x])] for x in input_file])
    result_choice_pt2 = ([response[(strategy_pt_2[x])[-1]] for x in input_file])
    result_pt2 = sum(result_match_pt2) + sum(result_choice_pt2)

    print("Part2:", result_pt2)

if __name__ == '__main__':
    main()
