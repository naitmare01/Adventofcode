#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import networkx as nx
import matplotlib.pyplot as plt

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Tree: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self):
        self.name = None
        self.unformated_tree = []

    def format_data(self, raw_data):
        for row in raw_data:
            row = row.split(" ")
            row.pop(1)
            if len(row) > 1:
                row.pop(1)
                self.unformated_tree.append(row)

    def draw_tree(self):
        graph = nx.DiGraph()
        for node in self.unformated_tree:
            root = node[0]
            edges = node[1:]
            graph.add_node(root)
            for edge in edges:
                graph.add_edge(root, edge)
        nx.draw(graph, with_labels=True)
        plt.draw()
        plt.show()

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().split("\n")

    tree = Tree()
    tree.format_data(input_file)
    tree.draw_tree()
    #print(tree.unformated_tree)

if __name__ == '__main__':
    main()
