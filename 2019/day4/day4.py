#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=False)

    args = parser.parse_args()

    return args

def filter_adjacent_digits(number_range):
    result = []
    for number_filter in range(0, 10):
        filter_number = (str(number_filter) + str(number_filter))
        result.append(list(filter(lambda x: filter_number in str(x), number_range)))
    return result

def check_same_increase(number):
    num = str(number)
    for i in range(5):
        if int(num[i+1]) < int(num[i]):
            return False
    return True

def convert_list_to_int(int_list):
    # Converting integer list to string list
    step_one = [str(i) for i in int_list]

    # Join list items using join()
    res = int("".join(step_one))

    return res

def filter_decrease_digits(number_list):
    result = []
    for tenth in number_list:
        for number in tenth:
            if check_same_increase(number):
                result.append(number)
    return result

def solve_it(part):
    potentials = []
    for i in range(193651, 649729):
        potentials.append(str(i))

    passedfirst = []
    for item in potentials:
        if list(item) == sorted(item):
            passedfirst.append(item)

    passedsecond = []
    for number in passedfirst:
        for digit in number:
            count = number.count(digit)
            if part == "two":
                if count == 2: #change this to '==' for part 2 (srsly)
                    passedsecond.append(number)
                    break
            elif part == "one":
                if count >= 2: #change this to '==' for part 2 (srsly)
                    passedsecond.append(number)
                    break

    print(len(passedsecond))

def main():
    #args = arguments()
    #puzzle_input = range(193651, 649729)
    #puzzle_input = range(100, 200)
    #filter_list = filter_adjacent_digits(puzzle_input)
    #print(len(filter_decrease_digits(filter_list)))
    solve_it("one")
    solve_it("two")



if __name__ == '__main__':
    main()
