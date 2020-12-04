#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Md5Sum: # pylint: disable=too-few-public-methods
    def __init__(self):
        self.all_frequency = []
        self.md5sum = None
        self.prototype_fabric_box = []
        self.common_letters = None

    def count_frequency(self, list_of_words):
        for test_str in list_of_words:
            all_freq = {}

            for i in test_str:
                if i in all_freq:
                    all_freq[i] += 1
                else:
                    all_freq[i] = 1
            self.all_frequency.append(all_freq)

    def calculate_md5(self):
        all_letters_appearing_twice = list(filter(lambda x: {k:v for k, v in x.items() if v == 2}, self.all_frequency))
        all_letters_appearing_thrice = list(filter(lambda x: {k:v for k, v in x.items() if v == 3}, self.all_frequency))
        self.md5sum = len(all_letters_appearing_twice) * len(all_letters_appearing_thrice)

    def calculate_prototype_fabric(self, list_of_words):
        for word in list_of_words:
            for word_two in list_of_words:
                zipped = zip(word, word_two)
                duplicates = list(filter(lambda pair: pair[0] == pair[1], zipped))
                if len(duplicates) == len(word) - 1:
                    common_letters = ''.join(pair[0] for pair in duplicates)
                    self.prototype_fabric_box.append(word)
                    self.prototype_fabric_box.append(word_two)
                    self.common_letters = common_letters
                    return

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().splitlines()

    md5sum = Md5Sum()
    md5sum.count_frequency(input_file)
    md5sum.calculate_md5()
    print("Part1:", md5sum.md5sum)
    md5sum.calculate_prototype_fabric(input_file)
    print("Part2 boxes:", md5sum.prototype_fabric_box)
    print("Part2 common letters:", md5sum.common_letters)

if __name__ == '__main__':
    main()
