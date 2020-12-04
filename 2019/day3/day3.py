#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

def movement(list_of_movements):
    movement_pattern = [[0, 0]] #same as R8,U5,L5,D3 but with co-ordinates
    location_on_map = [0, 0] #holds the end location on the map
    path = [[0, 0]] #displays all the stops during the trip.

    for move in list_of_movements:
        steps = int(move[1:])
        heading = move[:1]

        if heading.upper() == "R":
            location_on_map[0] = (location_on_map[0] + steps)
            new_x_location = (movement_pattern[0][0] + steps)
            current_y_location = movement_pattern[0][1]
            movement_pattern.append([new_x_location, current_y_location])

        if heading.upper() == "L":
            location_on_map[0] = (location_on_map[0] - steps)
            new_x_location = (movement_pattern[0][0] - steps)
            current_y_location = movement_pattern[0][1]
            movement_pattern.append([new_x_location, current_y_location])

        if heading.upper() == "U":
            location_on_map[1] = (location_on_map[1] + steps)
            new_y_location = (movement_pattern[0][1] + steps)
            current_x_location = movement_pattern[0][0]
            movement_pattern.append([current_x_location, new_y_location])

        if heading.upper() == "D":
            location_on_map[1] = (location_on_map[1] - steps)
            new_y_location = (movement_pattern[0][1] - steps)
            current_x_location = movement_pattern[0][0]
            movement_pattern.append([current_x_location, new_y_location])
        path.append([location_on_map[0], location_on_map[1]])

    print(movement_pattern)
    #print(path)
    #print(location_on_map)

def get_path(wire):
    i = j = 0
    step = 1
    path = {}
    for visit in wire:
        direction, position = visit[0], int(visit[1:])
        x_position = y_position = 0
        if direction == 'U':
            x_position = -1
        elif direction == 'D':
            x_position = 1
        elif direction == 'L':
            y_position = -1
        elif direction == 'R':
            y_position = 1
        else:
            raise Exception('Unexpected direction')

        for _ in range(position):
            i += x_position
            j += y_position
            path[(i, j)] = step
            step += 1

    return path

def get_intersections(path_one, path_two):
    result = list(set(path_one.keys()) & set(path_two.keys()))

    return result

def calculate_distance(location, goal):
    min_distance = []
    for cord in location:
        result = abs(cord[0] - goal[0]) + abs(cord[1] - goal[1])
        min_distance.append(result)

    result = min(min_distance)
    return result

def calculate_min_steps(intersections, steps_a, steps_b):
    min_steps = float('inf')
    for point in intersections:
        if point not in steps_a or point not in steps_b:
            raise Exception('Not an shared path intersection.')
        min_steps = min(min_steps, steps_a[point] + steps_b[point])
    return min_steps

def main():
    args = arguments()
    result = []
    with open(args.file) as input_file:
        for line in input_file:
            result.append(get_path(line.split(",")))
            if 'str' in line:
                break

    intersections = get_intersections(result[0], result[1])
    print(calculate_distance(intersections, (0, 0))) #part one
    print(calculate_min_steps(intersections, result[0], result[1])) #part two


if __name__ == '__main__':
    main()
