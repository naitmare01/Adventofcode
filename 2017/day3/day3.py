#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class SpiralMemory: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self, end):
        self.end = end
        self.end_cords = None
        self.map = [(0, 0)] #position 1
        self.manhattan_distance = None
        self.closet_cord_to_end = None
        self.shell_sides = None
        self.first_cell_cords = None
        self.first_cell_value = None

    def find_shell_of_spiral(self):
        total_cords = 1
        shell = 1
        shell_number = 1
        first_cell_cords = (0, 0)
        while total_cords <= self.end:
            first_cell_cords = ((first_cell_cords[0] + 1), (first_cell_cords[1] -1))
            total_cords = total_cords + ((shell + 2) * 2) + shell * 2
            shell = shell + 2
            shell_number = shell_number + 1
            shell_sides = [shell, shell - 2, shell, shell - 2]
            shell_start_value = total_cords - sum(shell_sides) + 1
            shell_start_cords = ((first_cell_cords[0]), (first_cell_cords[1] + 1))
            values = (total_cords, shell_start_value)
            closet_cord = min(values, key=lambda v: abs(self.end-v))

        self.shell_sides = shell_sides
        self.first_cell_cords = first_cell_cords

        if closet_cord == shell_start_value:
            self.closet_cord_to_end = shell_start_cords
            self.first_cell_value = shell_start_value
        else:
            self.closet_cord_to_end = first_cell_cords
            self.first_cell_value = total_cords

    def traverse_shell(self):
        cell_value = self.first_cell_value
        self.end_cords = self.closet_cord_to_end
        for idx, sides in enumerate(self.shell_sides):
            for num in range(sides): #pylint: disable=unused-variable
                if cell_value == self.end: #pytlint: disable=no-else-return
                    return
                else:
                    new_x = self.end_cords[0]
                    new_y = self.end_cords[1]

                    if idx == 0:
                        #print("Go left")
                        new_x = new_x - 1
                    elif idx == 1:
                        #print("go up")
                        new_x = new_y + 1
                    elif idx == 2:
                        #print("go right")
                        new_x = new_x + 1
                    elif idx == 3:
                        #print("go down")
                        new_x = new_y - 1

                self.end_cords = (new_x, new_y)
                cell_value = cell_value - 1

    def calculate_manhattan_distance(self):
        '''For example, if 𝑥=(𝑎,𝑏) and 𝑦=(𝑐,𝑑), the Manhattan distance between 𝑥 and 𝑦 is
        |𝑎−𝑐|+|𝑏−𝑑|.'''
        self.manhattan_distance = abs(self.end_cords[0] - self.map[0][0]) + abs(self.end_cords[1] - self.map[0][1])

    def draw_map_old(self):
        direction = "R"
        index = 0
        while len(self.map) < self.end:
            index = index + 1
            if direction == "R":
                new_x = self.map[index - 1][0] + 1
                new_y = self.map[index - 1][1]

                empty_space_to_up = (new_x, new_y + 1)
                if empty_space_to_up not in self.map:
                    direction = "U"
            elif direction == "U":
                new_x = self.map[index - 1][0]
                new_y = self.map[index - 1][1] + 1

                empty_space_to_left = (new_x - 1, new_y)
                if empty_space_to_left not in self.map:
                    direction = "L"
            elif direction == "L":
                new_x = self.map[index - 1][0] - 1
                new_y = self.map[index - 1][1]

                empty_space_to_down = (new_x, new_y - 1)
                if empty_space_to_down not in self.map:
                    direction = "D"
            elif direction == "D":
                new_x = self.map[index - 1][0]
                new_y = self.map[index - 1][1] - 1

                empty_space_to_right = (new_x + 1, new_y)
                if empty_space_to_right not in self.map:
                    direction = "R"

            self.map.append((new_x, new_y))

    def draw_map(self):
        #1 höger, 1 upp, 2 vänster, 2 ner, 3 höger, 3, upp osv
        index = 0
        steps = 1
        while len(self.map) < self.end:
            print(steps)
            for step in range(steps):
                if steps % 2 != 0:
                    new_x = self.map[index][0] + 1
                    new_y = self.map[index][1]
                    self.map.append((new_x, new_y)) #go right

                    index = index + 1

                    new_x = self.map[index][0]
                    new_y = self.map[index][1] + 1
                    self.map.append((new_x, new_y)) #go up

                    index = index + 1

                elif steps % 2 == 0:
                    new_x = self.map[index][0] - 1
                    new_y = self.map[index][1]
                    self.map.append((new_x, new_y)) #go left

                    index = index + 1

                    new_x = self.map[index][0]
                    new_y = self.map[index][1] - 1
                    self.map.append((new_x, new_y)) #go down

                    index = index + 1

            steps = steps + 1

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip("\t").split("\n")
        input_file = [int(x) for x in input_file]

    spiral_memory = SpiralMemory(input_file[0])
    spiral_memory.find_shell_of_spiral()
    spiral_memory.traverse_shell()
    spiral_memory.calculate_manhattan_distance()
    print("part1:", spiral_memory.manhattan_distance)

    #part2
    spiral_memory.draw_map()
    print(spiral_memory.map)

if __name__ == '__main__':
    main()
