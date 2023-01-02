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
            "RU": [1, 1], # Right-UP
            "DL": [-1, -1], # Down-Left
            "LU": [-1, 1], # Left-UP
            "DR": [1, -1], # Down-Right
        }
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
                            if self.knots[idx][0] < leader[0] and self.knots[idx][1] < leader[1]:
                                diag_direction = "RU"
                            elif self.knots[idx][0] > leader[0] and self.knots[idx][1] > leader[1]:
                                diag_direction = "DL"
                            elif self.knots[idx][0] > leader[0] and self.knots[idx][1] < leader[1]:
                                diag_direction = "LU"
                            elif self.knots[idx][0] < leader[0] and self.knots[idx][1] > leader[1]:
                                diag_direction = "DR"
                            else:
                                print("Error", self.knots[idx], leader)
                            self.knots[idx] = ([sum(x) for x in zip(self.knots[idx], self.directions[diag_direction])])
                self.last_leader_pos = leader
            self.visited.add(tuple(self.knots[-1]))

    def adjac(self, ele, sub = []):
        '''Adj'''
        if not ele:
            yield sub
        else:
            yield from (idx for j in range(ele[0] - 1, ele[0] + 2) for idx in self.adjac(ele[1:], sub + [j]))

class SnakeComplete:
    '''Snake'''
    def __init__(self):
        self.knots = None
        self.directions = {
            "U": (1, 0),
            "D": (-1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }
        self.visited = {(0, 0)}

    def reset(self, number_of_knots):
        '''Reset'''
        self.knots = [[0, 0] for _ in range(number_of_knots)]

    def travel(self, instruction):
        '''Travel'''
        direction, num_steps = instruction[0], int(instruction[1])
        for _ in range(num_steps):
            direction_y, direction_x = self.directions[direction]
            self.knots[0][0] += direction_y
            self.knots[0][1] += direction_x
            for _, tail in enumerate(self.knots):
                direction_y = self.knots[tail -1 ][0] - self.knots[tail][0]
                direction_x = self.knots[tail -1 ][1] - self.knots[tail][1]
                if max(abs(direction_y), abs(direction_x)) > 1:
                    self.knots[tail][0] += direction_y // abs(direction_y) if direction_y else 0
                    self.knots[tail][1] += direction_x // abs(direction_x) if direction_x else 0
                self.visited.add(tuple(self.knots[-1]))


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = (x.split(" ") for x in input_file)
    snake = Snake()
    snake.reset(1)

    snake_complete = SnakeComplete()
    snake_complete.reset(9)
    for row in input_file:
        snake.travel(row)
        snake_complete.travel(row)
    print("Part1:", len(snake.visited))
    print("Part2:", len(snake_complete.visited))



if __name__ == '__main__':
    main()
