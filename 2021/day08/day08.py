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

# int: number of lines to light up
NUMBER_OF_LINES = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

class Decoder:
    '''Decoder'''
    def __init__(self):
        self.instruction = None
        self.digit = None
        self.number_output_values_part1 = 0

    def find_digits(self, digit):
        '''Find digits'''
        for row in self.instruction:
            words = row[1].split()
            word_len = [NUMBER_OF_LINES[x] for x in digit]
            self.number_output_values_part1 += (len(self.intersection([len(x) for x in words], word_len)))

    def find_digits_part2(self):
        '''Find digits part 2'''
        for row in self.instruction:
            words = row[1].split()
            word_list = row[0].split()
            digitmap = dict()

            unique_numbers = [1, 4, 7, 8]
            for num in unique_numbers:
                digitmap[num] = ("".join([x for x in word_list if len(x) == NUMBER_OF_LINES[num]][0]))

            all_five_len_word = [x for x in word_list if len(x) == NUMBER_OF_LINES[5]]
            all_six_len_word = [x for x in word_list if len(x) == NUMBER_OF_LINES[6]]

            digitmap[2] = "".join([x for x in all_five_len_word if digitmap[1][1] not in x][0])
            digitmap[3] = "".join([x for x in all_five_len_word if digitmap[1][1] in x and digitmap[1][0] in x][0])
            digitmap[5] = "".join([x for x in all_five_len_word if digitmap[1][0] not in x][0])
            digitmap[9] = "".join(([x for x in all_six_len_word if set(digitmap[4]) <= set(x)][0]))
            zero_or_six = ([x for x in all_six_len_word if set(digitmap[4]) - set(x)])
            digitmap[6] = "".join([x for x in zero_or_six if digitmap[1][0] not in x])
            digitmap[0] = "".join([x for x in zero_or_six if digitmap[1][0] in x])

            print([self.get_key(x, digitmap) for x in words])
            print([x for x in words], digitmap)

            # börja med att sätta alla unika. 1, 4, 7, 8

            # 5 tecken, utgå ifrån 1 och börja mappa. Leta efter 2 och sedan 3 och 5.
            # 1.1 kan vara en 2 eller 3. Om 1.2 är samma så är det en 3. Annars 2.
            # Om 1.2 är samma så är det en 5.

            # 6 tecken, utgå ifrån 1 och börja mappa 9, 6 och 0
            # Om enbart 1.2 är det en sexa.
            # Kolla om alla tecken i 4an finns med. Om ja så är det en 9a, annars en sexa.

    def intersection(self, lst1, lst2):
        '''Intersection'''
        temp = set(lst2)
        lst3 = [value for value in lst1 if value in temp]
        return lst3

    def get_key(self, val, my_dict):
        for key, value in my_dict.items():
            if val == value:
                return key


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.split('\n')
        input_file = [x.split(' | ') for x in input_file]
    decoder = Decoder()
    decoder.instruction = input_file
    part1_digits = [1, 4, 7, 8]
    decoder.find_digits(part1_digits)
    print("Part1:", decoder.number_output_values_part1)

    decoder = Decoder()
    decoder.instruction = input_file
    decoder.find_digits_part2()

if __name__ == '__main__':
    main()
