#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class InverseCaptcha: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self):
        self.captcha_part1 = 0
        self.captcha_part2 = 0

    def calculate_captcha_part1(self, number):
        for idx, num in enumerate(number):
            if idx == (len(number) - 1):
                if num == number[0]:
                    self.captcha_part1 = self.captcha_part1 + int(num)
            elif num == number[idx + 1]:
                self.captcha_part1 = self.captcha_part1 + int(num)

    def calculate_captcha_part2(self, number):
        halfway_marker = int(len(number) / 2)
        for idx, num in enumerate(number):
            idx_position = idx + halfway_marker
            if idx_position >= len(number):
                idx_position = idx_position - len(number)
            if num == number[idx_position]:
                self.captcha_part2 = self.captcha_part2 + int(num)

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()

    captcha = InverseCaptcha()
    captcha.calculate_captcha_part1(input_file)
    captcha.calculate_captcha_part2(input_file)
    print("part1:", captcha.captcha_part1) #part1
    print("part2:", captcha.captcha_part2) #part1

if __name__ == '__main__':
    main()
