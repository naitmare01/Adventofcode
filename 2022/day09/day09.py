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
        self.knots = None
        self.visited = {(0, 0)}
        self.directions = {
            "R": [0, 1],
            "L": [0, -1],
            "U": [1, 0],
            "D": [-1, 0],
        }
        self.last_head_pos = None
        self.last_leader_pos = None

    def reset(self, num_knots):
        self.knots = [[0, 0] for x in range(num_knots)]

    def travel(self, instruction):
        '''Travel'''
        direction, num_steps = instruction[0], int(instruction[1])
        for _ in range(num_steps):
            self.head_pos = [sum(x) for x in zip(self.head_pos, self.directions[direction])]
            for idx, _ in enumerate(self.knots):
                if idx == 0:
                    leader = self.head_pos
                else:
                    leader = self.knots[idx - 1]

                if leader != self.knots[idx]:
                    adjacent_pos = list(self.adjac(self.knots[idx]))
                    if len([x for x in adjacent_pos if x == leader]) == 0:
                        if self.knots[idx][0] == leader[0] or self.knots[idx][1] == leader[1]:
                            self.knots[idx] = [sum(x) for x in zip(self.knots[idx], self.directions[direction])]
                        else:
                            self.knots[idx] = self.last_leader_pos # Diag move to last_head_pos
                self.last_leader_pos = leader
            self.visited.add(tuple(self.knots[-1]))

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
    snake.reset(1)
    snake_pt2 = Snake()
    snake_pt2.reset(9)
    for _, row in enumerate(input_file):
        snake.travel(row)
        snake_pt2.travel(row)
    print("Part1:", len(snake.visited))
    print("Part2:", len(snake_pt2.visited))



if __name__ == '__main__':
    main()
