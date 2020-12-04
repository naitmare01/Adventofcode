#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class TestPassword():
    def __init__(self):
        self.Password = None
        self.Valid_p1 = False
        self.Valid_p2 = False
        self.validator = None
        self.min_number = 0
        self.max_number = 0

    def test_valid(self):
        number_of_validator = self.Password.count(self.validator)
        if self.min_number <= number_of_validator <= self.max_number:
            self.Valid_p1 = True

        index_matches = 0
        if self.Password[self.min_number - 1] is self.validator:
            index_matches += 1
        if self.Password[self.max_number - 1] is self.validator:
            index_matches += 1
        if index_matches == 1:
            self.Valid_p2 = True


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    result = []
    for row in input_file:
        class_password = TestPassword()
        class_password.Password = (row.split(' '))[-1]
        class_password.validator = ((row.split(' '))[1])[0]
        class_password.min_number = int((row.split(' ')[0]).split('-')[0])
        class_password.max_number = int((row.split(' ')[0]).split('-')[1])
        class_password.test_valid()
        result.append(class_password)

    print("Part1:", len([x for x in result if x.Valid_p1 is True]))
    print("Part2:", len([x for x in result if x.Valid_p2 is True]))


if __name__ == '__main__':
    main()
