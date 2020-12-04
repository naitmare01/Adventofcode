#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from collections import deque

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class TreeOld: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self):
        self.result = None
        self.metadata_entries = []

    def calculate_metadata(self, input_list):
        index = 0
        while input_list:
            has_childnodes = input_list[index]
            num_of_metadata = input_list[index + 1]
            if len(input_list) < (num_of_metadata - 2):
                break

            if has_childnodes > 0:
                metadata_entries = input_list[-num_of_metadata:]
                input_list.pop(index) #remove info about child nodes
                input_list.pop(index) #remove info about num of metadata entries
                for num in range(num_of_metadata): #remove all metadata entries
                    input_list.pop(-1)
            else:
                input_list.pop(index) #remove info about child nodes
                input_list.pop(index) #remove info about num of metadata entries
                metadata_entries = input_list[index:(num_of_metadata)]
                for num in range(num_of_metadata): #remove all metadata entries
                    input_list.pop(index)

            for num in metadata_entries:
                self.metadata_entries.append(num)

class Tree: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self, data):
        self.n_children = data.popleft()
        self.n_metadata = data.popleft()
        self.children = [Tree(data) for _ in range(self.n_children)]
        self.metadata = [data.popleft() for _ in range(self.n_metadata)]

    def calculate_metadata(self):
        return sum(self.metadata) + sum(child.calculate_metadata() for child in self.children)

    def get_child_value(self, child):
        if child < len(self.children):
            return self.children[child].get_root_value()
        return 0

    def get_root_value(self):
        if not self.children:
            return sum(self.metadata)
        total = 0
        for idx in self.metadata:
            total += self.get_child_value(idx - 1) # Index starts at 1 not 0 :(
        return total

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().split(" ")
        data = deque()
        for line in input_file:
            for val in line.split(' '):
                data.append(int(val))
        input_file = list((int(number) for number in input_file))

    tree = Tree(data)
    print("part1:", tree.calculate_metadata())
    print("part2:", tree.get_root_value())



if __name__ == '__main__':
    main()
