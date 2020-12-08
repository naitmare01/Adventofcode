#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import networkx as nx


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Haversacks():
    def __init__(self):
        self.tree = None
        self.number_of_preds = None

    def build_tree(self, bags):
        self.tree = nx.DiGraph()
        self.tree.add_edges_from(bags)

    def find_all_preds(self, child_bag):
        tocheck = set(self.tree.predecessors(child_bag))
        preds = set()
        while tocheck:
            node = tocheck.pop()
            preds.add(node)
            tocheck.update(set(self.tree.predecessors(node)).difference(preds))
        self.number_of_preds = len(preds)

    def count_inners(self, bag):
        print(list(nx.edge_dfs(self.tree, bag)))


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    graph_edges = []
    for row in input_file:
        parent, tokens = [s for s in row.split(' bags contain ')]
        for token in tokens.replace('.', '').split(', '):
            if token != 'no other bags':
                child = token[2:].split(' bag')[0].strip()
                graph_edges.append((parent, child))

    haversacks = Haversacks()
    haversacks.build_tree(graph_edges)
    haversacks.find_all_preds('shiny gold')
    haversacks.count_inners('shiny gold')
    print("Part1:", haversacks.number_of_preds)
    print("Part2:", haversacks.__dict__)


if __name__ == '__main__':
    main()
