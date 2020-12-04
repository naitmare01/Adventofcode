#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse

class Layer:
    def __init__(self, name):
        self.name = name
        self.numbers = None
        self.number_of_zeroes = None
        self.number_of_ones = None
        self.number_of_twos = None

    def add_numbers(self, numbers):
        self.numbers = numbers

    def count_number_of_zeroes(self):
        self.number_of_zeroes = self.numbers.count("0")

    def count_number_of_ones(self):
        self.number_of_ones = self.numbers.count("1")

    def count_number_of_twos(self):
        self.number_of_twos = self.numbers.count("2")


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-x', '--wide', required=True)
    parser.add_argument('-y', '--tall', required=True)

    args = parser.parse_args()

    return args

def split_n_char(string_to_convert, n_characther):
    result = [string_to_convert[i:i+n_characther] for i in range(0, len(string_to_convert), n_characther)]
    return result

def create_layer_object(layers):
    part1_result = []
    for idx, layer in enumerate(layers):
        layer_class = Layer(idx)
        layer_class.add_numbers(layer)
        layer_class.count_number_of_zeroes()
        part1_result.append(layer_class)
    return part1_result

def find_smallest_number_of_zeroes(layers):
    sorted_list = sorted(layers, key=lambda x: x.number_of_zeroes, reverse=False)
    return sorted_list[0]

def calculate_corruption(layer):
    #count number of ones and twos.
    layer.count_number_of_ones()
    layer.count_number_of_twos()

    checksum = layer.number_of_ones * layer.number_of_twos

    return checksum

def main():
    args = arguments()

    with open(args.file) as input_file:
        for line in input_file:
            layers = split_n_char(line, (int(args.wide) * int(args.tall)))
    part1 = create_layer_object(layers)
    part1smallest = find_smallest_number_of_zeroes(part1)
    part1checksum = calculate_corruption(part1smallest)
    print("Part1:", part1checksum) #Part 1

    for part in part1:
        print(part.numbers)
        for num in part.numbers:
            if num == "0":
                print(" ")
            elif num == "1":
                print("X")
            #print(color)

if __name__ == '__main__':
    main()

#Part 2
#Svart(0) || vit(1) > transparent(2)
