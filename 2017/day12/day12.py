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

class BinaryTree: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    def __init__(self):
        self.tree = nx.Graph()

    def draw_tree(self, lines):
        for line in lines:
            # Parse the line
            node, neighbors = line.split(' <-> ')
            # Add edges defined by this line
            self.tree.add_edges_from((node, neighbor) for neighbor in neighbors.split(', '))

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().split("\n")

    tree = BinaryTree()
    tree.draw_tree(input_file)
    part1_result = len(nx.node_connected_component(tree.tree, "0"))
    print("part1:", part1_result)
    print("part2:", nx.number_connected_components(tree.tree))

if __name__ == '__main__':
    main()
