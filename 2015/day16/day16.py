#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Aunt():
    def __init__(self):
        self.name = "Sue"
        self.gifts = {}
        self.gifting_aunt = False
        self.gifting_aunt_part2 = False

    def compare_gifts(self, gift_list):
        if all(item in gift_list.items() for item in self.gifts.items()):
            self.gifting_aunt = True
        if any(item in gift_list.items() for item in self.gifts.items()):
            # In particular, the cats and trees readings indicates that there are greater than that many in the gift list.
            # while the pomeranians and goldfish readings indicate that there are fewer than that many
            keys_to_remove = []
            for key in self.gifts:
                if key == "cats" and self.gifts[key] > gift_list[key]:
                    keys_to_remove.append(key)
                if key == "trees" and self.gifts[key] > gift_list[key]:
                    keys_to_remove.append(key)
                if key == "pomeranians" and self.gifts[key] < gift_list[key]:
                    keys_to_remove.append(key)
                if key == "goldfish" and self.gifts[key] < gift_list[key]:
                    keys_to_remove.append(key)
            for keys in keys_to_remove:
                self.gifts.pop(keys)
            if all(item in gift_list.items() for item in self.gifts.items()):
                self.gifting_aunt_part2 = True


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    part1_aunts = []
    gifts = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    for row in input_file:
        split_data = (row.split(':'))
        gifts_split = row.split(' ')
        gifts_name = [gifts_split[2][:-1], gifts_split[4][:-1], gifts_split[6][:-1]]
        gifts_value = [gifts_split[3], gifts_split[5], gifts_split[7]]
        gifts_value = [x.replace(',', '') for x in gifts_value]
        gifts_value = [int(x) for x in gifts_value]
        gifts_full_values = dict(zip(gifts_name, gifts_value))

        id = (split_data[0]).split()[1]
        aunt = Aunt()
        aunt.id = id
        aunt.gifts = gifts_full_values
        aunt.compare_gifts(gifts)
        part1_aunts.append(aunt)

    part1 = [x.id for x in part1_aunts if x.gifting_aunt is True]
    print("Part1:", part1[0])

    part2 = [x for x in part1_aunts if x.gifting_aunt_part2 is True and x.gifting_aunt is False]
    for aunts in part2:
        print("Part2:", aunts.id)


if __name__ == '__main__':
    main()
