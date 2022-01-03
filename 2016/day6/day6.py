#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    part1 = ""
    part2 = ""
    new_result = list(map(list, zip(*input_file)))
    for row in new_result:
        most_common = char_frequency(listToString(row))
        most_common = {k: v for k, v in sorted(most_common.items(), key=lambda item: item[1], reverse=True)}
        most_common_part2 = {k: v for k, v in sorted(most_common.items(), key=lambda item: item[1])}

        dict_pairs = most_common.items()
        pairs_iterator = iter(dict_pairs)
        first_pair = next(pairs_iterator)
        part1 += first_pair[0]

        dict_pairs_part2 = most_common_part2.items()
        pairs_iterator_part2 = iter(dict_pairs_part2)
        first_pair_part2 = next(pairs_iterator_part2)
        part2 += first_pair_part2[0]

    print(part1)
    print(part2)


if __name__ == '__main__':
    main()
