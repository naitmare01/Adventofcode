#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import networkx as nx

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Instructions: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self):
        self.result = None

    def calculate_order(self, lines):
        nxgraph = nx.DiGraph()
        for line in lines:
            parts = line.split(" ")
            nxgraph.add_edge(parts[1], parts[7])
        self.result = (''.join(nx.lexicographical_topological_sort(nxgraph)))

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().splitlines()
    instructions = Instructions()
    instructions.calculate_order(input_file)
    print("Part1:", instructions.result)

if __name__ == '__main__':
    main()
