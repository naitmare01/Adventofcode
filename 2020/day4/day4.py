#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import re


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Passport():
    def __init__(self):
        self.valid_pt1 = True
        self.valid_pt2 = True
        self.byr = None  # (Birth Year) - four digits; at least 1920 and at most 2002.
        self.iyr = None  # (Issue Year) - four digits; at least 2010 and at most 2020.
        self.eyr = None  # (Expiration Year) - four digits; at least 2020 and at most 2030.
        self.hgt = None  # (Height) - a number followed by either cm or in:, If cm, the number must be at least 150 and at most 193., If in, the number must be at least 59 and at most 76.
        self.hcl = None  # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        self.ecl = None  # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        self.pid = None  # (Passport ID) - a nine-digit number, including leading zeroes.
        self.cid = None  # (Country ID) - ignored, missing or not.

    def insert_values(self, attributes):
        if "byr" in attributes:
            self.byr = attributes["byr"]
        if "iyr" in attributes:
            self.iyr = attributes["iyr"]
        if "eyr" in attributes:
            self.eyr = attributes["eyr"]
        if "hgt" in attributes:
            self.hgt = attributes["hgt"]
        if "hcl" in attributes:
            self.hcl = attributes["hcl"]
        if "ecl" in attributes:
            self.ecl = attributes["ecl"]
        if "pid" in attributes:
            self.pid = attributes["pid"]
        if "cid" in attributes:
            self.cid = attributes["cid"]

        if (bool({k: v for k, v in self.__dict__.items() if k != 'cid' and k != 'valid_pt1' and v is None})):
            self.valid_pt1 = False

    def insert_values_pt2(self, attributes):
        if "byr" in attributes:
            if 1920 <= int(attributes["byr"]) <= 2002:
                self.byr = attributes["byr"]
        if "iyr" in attributes:
            if 2010 <= int(attributes["iyr"]) <= 2020:
                self.iyr = attributes["iyr"]
        if "eyr" in attributes:
            if 2020 <= int(attributes["eyr"]) <= 2030:
                self.eyr = attributes["eyr"]
        if "hgt" in attributes:
            if "cm" in attributes["hgt"]:
                hgt = int((attributes["hgt"].split('cm'))[0])
                if 150 <= hgt <= 193:
                    self.hgt = attributes["hgt"]
            else:
                hgt = int((attributes["hgt"].split('in'))[0])
                if 59 <= hgt <= 76:
                    self.hgt = attributes["hgt"]
        if "hcl" in attributes:
            if re.match('^#[0-9a-f]{6}$', attributes['hcl']):
                self.hcl = attributes["hcl"]
        if "ecl" in attributes:
            if attributes["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                self.ecl = attributes["ecl"]
        if "pid" in attributes:
            if re.match('^[0-9]{9}$', attributes['pid']):
                self.pid = attributes["pid"]
        if "cid" in attributes:
            self.cid = attributes["cid"]

        if (bool({k: v for k, v in self.__dict__.items() if k != 'cid' and k != 'valid_pt2' and v is None})):
            self.valid_pt2 = False


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = [dict(re.findall(r"(\S+):(\S+)", raw)) for raw in file.read().strip().split("\n\n")]

    result = []
    for row in input_file:
        passport = Passport()
        passport.insert_values(row)
        result.append(passport)

    print("Part1:", len([x for x in result if x.valid_pt1 is True]))

    result = []
    for row in input_file:
        passport = Passport()
        passport.insert_values_pt2(row)
        result.append(passport)

    print("Part2:", len([x for x in result if x.valid_pt2 is True]))


if __name__ == '__main__':
    main()
