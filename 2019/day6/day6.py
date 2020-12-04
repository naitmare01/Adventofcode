#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import networkx as nx
import matplotlib.pyplot as plt

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=False)
    parser.add_argument('-p', '--plot', action='store_true')

    args = parser.parse_args()

    return args

def draw_graph(puzzle_input):
    graph = nx.DiGraph()
    for line in puzzle_input:
        node = line.split(")")[0]
        edge = line.split(")")[1]
        graph.add_edge(edge, node)

    return graph

def count_predecessor(graph):
    number_of_predecessor = 0
    for node in graph.nodes():
        number_of_predecessor = number_of_predecessor + ((len(nx.predecessor(graph, node))) - 1)

    return number_of_predecessor

def find_shortest_path(graph, source, target):
    source = source.upper()
    target = target.upper()
    graph = graph.to_undirected()
    shortest_path = nx.astar_path_length(graph, source=source, target=target)-2

    return shortest_path

def main():
    args = arguments()

    with open(args.file) as input_file:
        lines = input_file.read().splitlines()
        result = draw_graph(lines)

    print("Part 1:", count_predecessor(result)) #part1
    print("Part 2:", find_shortest_path(result, "YOU", "SAN")) #part2

    if args.plot:
        nx.draw(result, with_labels=True)
        plt.show()


if __name__ == '__main__':
    main()
