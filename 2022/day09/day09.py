#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse


def arguments():
    '''args'''
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Snake:
    '''Snake'''
    def __init__(self):
        self.head_pos = [0, 0]
        self.tail_pos = [0, 0]
        self.visited = {(0, 0)}
        self.directions = {
            "R": [0, 1],
            "L": [0, -1],
            "U": [1, 0],
            "D": [-1, 0],
        }
        self.last_head_pos = None

    def travel(self, instruction):
        '''Travel'''
        direction, num_steps = instruction[0], int(instruction[1])
        for _ in range(num_steps):
            self.head_pos = [sum(x) for x in zip(self.head_pos, self.directions[direction])]

            if self.head_pos != self.tail_pos:
                adjacent_pos = list(self.adjac(self.tail_pos))
                if len([x for x in adjacent_pos if x == self.head_pos]) == 0:
                    if self.tail_pos[0] == self.head_pos[0] or self.tail_pos[1] == self.head_pos[1]:
                        self.tail_pos = [sum(x) for x in zip(self.tail_pos, self.directions[direction])]
                    else:
                        self.tail_pos = self.last_head_pos # Diag move to last_head_pos
            self.visited.add(tuple(self.tail_pos)) # Update visited tails location
            self.last_head_pos = self.head_pos

    def adjac(self, ele, sub = []):
        '''Adj'''
        if not ele:
            yield sub
        else:
            yield from (idx for j in range(ele[0] - 1, ele[0] + 2) for idx in self.adjac(ele[1:], sub + [j]))


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = (x.split(" ") for x in input_file)
    snake = Snake()
    for row in input_file:
            snake.travel(row)
    print("Part1:", len(snake.visited))


if __name__ == '__main__':
    main()
