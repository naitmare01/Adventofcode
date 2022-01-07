#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from copy import deepcopy
import collections


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def test_horizontal(instructions, part2):
    straight_lines = []
    for row in instructions:
        x1 = row[0][0]
        x2 = row[1][0]
        y1 = row[0][1]
        y2 = row[1][1]
        if x1 == x2 or y1 == y2:
            straight_lines.append(row)
    return straight_lines


def calculate_numbers(list_of_lines, part2):
    result = []
    for row in list_of_lines:
        x1 = int(row[0][0])
        x2 = int(row[1][0])
        y1 = int(row[0][1])
        y2 = int(row[1][1])
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                maxy = max(y1, y2)
                miny = min(y1, y2)
                all_y_values = (list(range(miny, maxy + 1, 1)))
                for val in all_y_values:
                    result.append((x1, val))
            else:
                maxX = max(x1, x2)
                minX = min(x1, x2)
                all_x_values = (list(range(minX, maxX + 1, 1)))
                for val in all_x_values:
                    result.append((val, y1))
        elif part2:
            if x1 < x2:  # Right
                if y1 > y2:  # up
                    #print("RU", row)
                    cord = [x1, y1]
                    end = [x2, y2]
                    while True:
                        result.append((cord[0], cord[1]))
                        if cord == end:
                            break
                        else:
                            cord[0] += 1
                            cord[1] -= 1
                else:  # down
                    # print("RD", row)
                    cord = [x1, y1]
                    end = [x2, y2]
                    while True:
                        result.append((cord[0], cord[1]))
                        if cord == end:
                            break
                        else:
                            cord[0] += 1
                            cord[1] += 1
            elif x1 > x2:  # left
                if y1 > y2:  # up
                    # print("LU", row)
                    cord = [x1, y1]
                    end = [x2, y2]
                    while True:
                        result.append((cord[0], cord[1]))
                        if cord == end:
                            break
                        else:
                            cord[0] -= 1
                            cord[1] -= 1
                else:  # down
                    # print("DL", row)
                    cord = [x1, y1]
                    end = [x2, y2]
                    while True:
                        result.append((cord[0], cord[1]))
                        if cord == end:
                            break
                        else:
                            cord[0] -= 1
                            cord[1] += 1
    return result


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
        input_file = [x.split(' -> ') for x in input_file]
        input_file = [[y.split(',') for y in x] for x in input_file]
    pt1_straight_lines = test_horizontal(input_file, False)
    pt1_result = calculate_numbers(pt1_straight_lines, False)
    print("Part1:", len([item for item, count in collections.Counter(pt1_result).items() if count > 1]))

    pt2_result = calculate_numbers(input_file, True)
    print("Part2:", len([item for item, count in collections.Counter(pt2_result).items() if count > 1]))


if __name__ == '__main__':
    main()
