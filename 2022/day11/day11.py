#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import re
import numpy

def arguments():
    '''args'''
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Monkey:
    '''Monkey'''
    def __init__(self):
        self.id = None
        self.items = []
        self.worry_operation = None # eval()
        self.test_divisible = None
        self.throw_true_monkey = None
        self.throw_false_monkey = None
        self.inspected_items = 0

    def test_worry_level(self, all_monkeys):
        '''Test'''
        for i in self.items:
            self.inspected_items += 1
            worry_level = int(eval(self.worry_operation.replace('old', i)) / 3)

            if worry_level % self.test_divisible == 0:
                throw_to = self.throw_true_monkey
            else:
                throw_to = self.throw_false_monkey
            all_monkeys[throw_to].items.append(str(worry_level))

        self.items = []

def parse_input(input_data):
    '''Parse input into nicer format'''
    monkey_and_attributes = (input_data.split('\n'))
    monkey_and_attributes = [x.strip() for x in monkey_and_attributes]
    monkey_and_attributes[0] = int(''.join(re.findall(r'\d+', monkey_and_attributes[0]))) # ID
    monkey_and_attributes[1] = re.findall(r'\d+', monkey_and_attributes[1]) # Items
    monkey_and_attributes[2] = monkey_and_attributes[2].split("Operation: new = ")[-1] # Worry Operation
    monkey_and_attributes[3] = int(''.join(re.findall(r'\d+', monkey_and_attributes[3]))) # Divisible
    monkey_and_attributes[4] = int(''.join(re.findall(r'\d+', monkey_and_attributes[4]))) # If true, monkey ID
    monkey_and_attributes[5] = int(''.join(re.findall(r'\d+', monkey_and_attributes[5]))) # If false, monkey ID
    return monkey_and_attributes

def main():
    '''Main'''
    args = arguments()
    with open(args.file, encoding="utf8") as file:
        input_file = file.read().strip()
        input_file = input_file.split('\n\n')

    all_monkeys = []
    for monkey in input_file:
        parsed_monkey = parse_input(monkey)
        monk = Monkey()
        all_monkeys.append(monk)
        monk.id = parsed_monkey[0]
        monk.items = parsed_monkey[1]
        monk.worry_operation = parsed_monkey[2]
        monk.test_divisible = parsed_monkey[3]
        monk.throw_true_monkey = parsed_monkey[4]
        monk.throw_false_monkey = parsed_monkey[5]
    num_rounds = 20
    for _ in range(num_rounds):
        _ = [x.test_worry_level(all_monkeys) for x in all_monkeys]
    result_pt1 = ([(x.inspected_items) for x in all_monkeys])
    result_pt1 = (sorted(result_pt1, reverse=True)[:2])
    print("Part1:", numpy.prod(result_pt1))


if __name__ == '__main__':
    main()
