#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class LoginScreen:  # pylint: disable=too-few-public-methods
    def __init__(self):
        self.screen = None

    def turn_on(self, cords):
        rows, cols = (4, 4)
        arr = [["."] * cols] * rows
        self.screen = arr

        update_cord = []
        for row in range(cords[0]):
            for col in range(cords[1]):
                update_cord.append([col, row])
                # self.screen[col][row] = "#"

        for cords in update_cord:
            print(cords[0], cords[1])
            self.screen[cords[0]][cords[1]] = "#"


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
    login_screen = LoginScreen()
    login_screen.turn_on((3, 2))
    print(login_screen.screen)


if __name__ == '__main__':
    main()
