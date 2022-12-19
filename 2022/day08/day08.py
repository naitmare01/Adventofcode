
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


def convert_1d_to_2d(l, cols):
    '''Matrix'''
    return [l[i:i + cols] for i in range(0, len(l), cols)]


def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()
    trees = {}
    for row_idx, row in enumerate(input_file):
        for col_idx, col in enumerate(row):
            if (row_idx - 1) == -1 or (col_idx -1 == -1):
                trees[row_idx, col_idx] = "True" # Edges
            else:
                try:
                    _ = input_file[row_idx + 1][col_idx + 1]
                    print("Pos:", row_idx, col_idx, "Value:", input_file[row_idx][col_idx])
                    for i in reversed(range(row_idx)): # Looking up
                        print(i)
                except IndexError:
                    trees[row_idx, col_idx] = "True" # Edges
    print(trees.__dir__)

if __name__ == '__main__':
    main()
