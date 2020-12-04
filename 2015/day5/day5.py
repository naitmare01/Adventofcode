#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import re
import collections

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class NiceString:
    def __init__(self, unknown_string):
        self.unknown_string = unknown_string
        self.number_of_vowels = 0
        self.nice_string = False
        self.nice_string_part2 = False
        self.matching_pair = False
        self.forbidden_strings = False
        self.pairs_appearing_twice = False
        self.pairs_appearing_overlapping = False

    def test_vowels(self):
        self.number_of_vowels = len([x for x in self.unknown_string if x in ('a', 'e', 'i', 'o', 'u')])

    def test_matchning_pair(self):
        matching_pair = [m.group() for m in re.finditer(r'((\w)\2)+', self.unknown_string)]
        if matching_pair:
            self.matching_pair = True

    def test_forbidding_strings(self):
        forbidden = ["ab", "cd", "pq", "xy"]
        fobidden_chars = [x for x in forbidden if x in self.unknown_string]
        if fobidden_chars:
            self.forbidden_strings = True

    def test_string(self):
        self.test_forbidding_strings()
        self.test_matchning_pair()
        self.test_vowels()
        self.count_pairs()

        if self.number_of_vowels >= 3:
            if self.matching_pair is True:
                if self.forbidden_strings is False:
                    self.nice_string = True

        if self.pairs_appearing_twice:
            if self.pairs_appearing_overlapping:
                self.nice_string_part2 = True

    def pairs_from_iterable(self, iterable):
        for index, item in enumerate(iterable):
            try:
                yield item, iterable[index + 1]
            except IndexError:
                return

    def pairs_from_iterable_overlapping(self, iterable):
        for index, item in enumerate(iterable):
            try:
                if item == iterable[index +2]:
                    yield item, iterable[index + 2]
            except IndexError:
                return

    def count_pairs(self):
        pairs = self.pairs_from_iterable(self.unknown_string)
        counter = collections.Counter(pairs)
        pairs_appearing_twice = {x: count for x, count in counter.items() if count >= 2}
        #print(pairs_appearing_twice)
        if pairs_appearing_twice:
            self.pairs_appearing_twice = True

        pairs_overlapping = self.pairs_from_iterable_overlapping(self.unknown_string)
        counter_overlapping = collections.Counter(pairs_overlapping)
        pairs_appearing_overlapping = {x: count for x, count in counter_overlapping.items() if count >= 1}
        #print(pairs_appearing_overlapping)
        if pairs_appearing_overlapping:
            self.pairs_appearing_overlapping = True

def is_nice2(password):
    if len(re.findall(r"([a-z]{2}).*\1", password)) and re.findall(
            r"([a-z]).\1", password
    ):
        return True
    return False

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    result = []
    result2 = []
    for row in input_file:
        test_string = NiceString(row)
        test_string.test_string()
        result.append(test_string)
        if is_nice2(row):
            result2.append(is_nice2)

    result_part1 = len([x for x in result if x.nice_string is True])
    print("Part 1:", result_part1)
    print("Part 2:", len(result2))

if __name__ == '__main__':
    main()


#Day 2


#with open('/path/to/file.txt') as source:
#    pairs = pairs_from_iterable(source)
#    counter = collections.Counter(pairs)
