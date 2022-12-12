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

def return_common_chars(s1, s2):
    '''common'''
    char_of_s1 = set(s1)
    char_of_s2 = set(s2)
    common_char = char_of_s1 & char_of_s2
    return common_char


def return_common_chars_pt2(s1, s2, s3):
    '''common2'''
    char_of_s1 = set(s1)
    char_of_s2 = set(s2)
    char_of_s3 = set(s3)
    common_char = char_of_s1 & char_of_s2 & char_of_s3
    return common_char


def ord_numbers(s):
    '''ord'''
    if s.islower():
        result = ord(s) - 96
    else:
        result = ord((s.lower())) - 96 + 26
    return result

def divide_chunks(l, n):
    '''Divide'''
    for i in range(0, len(l), n):
        yield l[i:i + n]


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
    splitted_strings = [(x[len(x)//2:], x[:len(x)//2]) for x in input_file]
    common_chars = [return_common_chars(x[0], x[1]) for x in splitted_strings]
    common_chars_values = [ord_numbers(" ".join(map(str,x))) for x in common_chars]
    result_pt1 = sum(common_chars_values)

    print("Part1:", result_pt1)

    splitted_pt2 = list(divide_chunks(input_file, 3))
    common_chars_pt2 = [return_common_chars_pt2(x[0], x[1], x[2]) for x in splitted_pt2]
    common_chars_values = [ord_numbers(" ".join(map(str,x))) for x in common_chars_pt2]
    result_pt2 = sum(common_chars_values)

    print("Part2:", result_pt2)

if __name__ == '__main__':
    main()
