#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Frequency: # pylint: disable=too-few-public-methods
    def __init__(self):
        self.starting_frequency = 0
        self.frequency = None
        self.first_duplicate = None

    def update_frequency(self, changing_frequency):
        self.frequency = self.starting_frequency
        for freq in changing_frequency:
            freq = str(freq)
            signs = freq[:1]
            number_freq = freq[1:]
            number_freq = int(number_freq)

            if signs == "+":
                self.frequency = self.frequency + number_freq
            elif signs == "-":
                self.frequency = self.frequency - number_freq

    def calibrate(self, changing_frequency):
        result = set([0])
        current_frequency = self.starting_frequency
        while True:
            for freq in changing_frequency:
                freq = str(freq)
                signs = freq[:1]
                number_freq = freq[1:]
                number_freq = int(number_freq)

                if signs == "+":
                    current_frequency = current_frequency + number_freq
                elif signs == "-":
                    current_frequency = current_frequency - number_freq

                if current_frequency in result:
                    self.first_duplicate = current_frequency
                    return
                result.add(current_frequency)

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().splitlines()

    frequency = Frequency()
    frequency.update_frequency(input_file)
    frequency.calibrate(input_file)
    print("Part1:", frequency.frequency)
    print("Part2:", frequency.first_duplicate)

if __name__ == '__main__':
    main()
