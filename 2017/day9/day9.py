#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class StreamProcessing: # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self, stream):
        self.stream = stream
        self.total_levels = 0
        self.states = []

    def calculate_levels(self):
        current_level = 1
        garbage = False
        false_signs = False

        for idx, row in enumerate(self.stream):
            if false_signs:
                false_signs = False
            elif row == "!":
                garbage = True
                false_signs = True
            elif garbage:
                if row == ">":
                    garbage = False
            else:
                if row == "<":
                    garbage = True
                    continue
                elif row == "{":
                    if self.stream[idx - 1] == "{":
                        current_level = current_level + 1
                    state = "open"
                    self.states.append((current_level, state))
                elif row == "}":
                    if self.stream[idx - 1] == "}":
                        current_level = current_level - 1
                    state = "closed"
                    #print(state)
                    #open_brackets_on_level = [x for x in self.states if x[0] == current_level and x[1] == "open"]
                    #print(open_brackets_on_level[-1][0])

                #elif row == ",":
                #    current_level = current_level - 1
                #elif row == "{":
                #    current_level = current_level + 1
                #    self.total_levels = self.total_levels + current_level
                #    self.states.append((current_level, "open"))
                #elif row == "}":
                    #self.states[-1] = (current_level, "closed")


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()

    stream = StreamProcessing(input_file)
    stream.calculate_levels()
    #print(stream.total_levels)
    #print(stream.states)
    d = open('input','r').read()
    dep = 0
    tot = 0
    gar = False
    i = 0
    garc = 0
    while i < len(d):
        val = d[i]
        if val == '!':
            i += 2
            continue

        if gar:
            if val == '>':
                gar = False
            else:
                garc += 1
        elif val == '<':
            gar = True
        elif val == '}':
            dep -= 1
        elif val == '{':
            dep += 1
            tot += dep
        i += 1

    print('p1: ', tot)
    print('p2: ', garc)

if __name__ == '__main__':
    main()
