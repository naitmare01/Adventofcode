#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class CustomCustoms():
    def __init__(self):
        self.answers = None

    def find_anwers(self, group):
        self.answers = (len(set(group.replace("\n", ""))))


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip().split("\n\n")
    result = []
    for row in input_file:
        custom_answers = CustomCustoms()
        custom_answers.find_anwers(row)
        result.append(custom_answers)
    print(sum([x.answers for x in result]))


if __name__ == '__main__':
    main()
