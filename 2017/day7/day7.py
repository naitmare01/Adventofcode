#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
# from copy import deepcopy
import time
import networkx as nx
import collections


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Tree():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.graph = nx.DiGraph()
        self.result_pt1 = None
        self.result_pt2 = None
        self.weights = {}

    def setup_tree(self):
        for line in self.instructions:
            name = line.split()[0]
            self.graph.add_node(name, weight=int(line.split()[1].strip('()')))

            if '->' in line:
                children = [n.strip() for n in line.split('->')[1].split(',')]

                for child in children:
                    self.graph.add_edge(name, child)

    def topological_sort(self):
        self.result_pt1 = list(nx.topological_sort(self.graph))

    def get_weight(self):
        for node in reversed(self.result_pt1):
            total = self.graph.nodes[node]['weight']
            counts = collections.Counter(self.weights[child] for child in self.graph[node])
            unbalanced = None

            for child in self.graph[node]:
                if len(counts) > 1 and counts[self.weights[child]] == 1:
                    unbalanced = child
                    break
                val = self.weights[child]
                total += self.weights[child]
            if unbalanced:
                diff = self.weights[unbalanced] - val
                self.result_pt2 = self.graph.nodes[unbalanced]['weight'] - diff
                break
            self.weights[node] = total


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
    tree = Tree()
    tree.instructions = input_file
    tree.setup_tree()
    tree.topological_sort()
    print(f'Part1: {tree.result_pt1[0]}')
    tree.get_weight()
    print(f'Part2: {tree.result_pt2}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
