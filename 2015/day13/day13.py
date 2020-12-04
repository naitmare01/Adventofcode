#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import itertools


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-p2', '--part2', action='store_true')

    args = parser.parse_args()

    return args


class Person():
    def __init__(self):
        self.Name = ""
        self.neighbours = {}
        self.happiness = 0

    def calculate_happiness(self, r_neighbour, l_neighbour):
        self.happiness = self.neighbours[r_neighbour] + self.neighbours[l_neighbour]


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip()
        input_file = input_file.splitlines()

    part1_persons = []
    persons_list = []
    for row in input_file:
        person_name = row.split()[0]
        if not [x.Name for x in part1_persons if x.Name == person_name]:
            new_person = Person()
            new_person.Name = person_name
            neighbours_info = [x for x in input_file if person_name in x.split()[0]]
            neighbours_name = [(x.split()[-1])[:-1] for x in neighbours_info]
            neighbours_value = [x.split()[2:4] for x in neighbours_info]
            for n in neighbours_value:
                if n[0] == 'lose':
                    n[1] = -(int(n[1]))
            neighbours_value = [int(x[1]) for x in neighbours_value]
            neighbours_full_info = dict(zip(neighbours_name, neighbours_value))
            new_person.neighbours = neighbours_full_info
            part1_persons.append(new_person)
            persons_list.append(person_name)

    if args.part2:
        new_person = Person()
        new_person.Name = "Part2"
        neighbours_name = [x.Name for x in part1_persons]
        neighbours_value = []
        for n in range(len(neighbours_name)):
            neighbours_value.append(0)
        neighbours_full_info = dict(zip(neighbours_name, neighbours_value))
        new_person.neighbours = neighbours_full_info

        for person in part1_persons:
            part2_neighbours = {'Part2': 0}
            person.neighbours = {**person.neighbours, **part2_neighbours}
        part1_persons.append(new_person)
        persons_list.append("Part2")

    all_permutations = (itertools.permutations(persons_list))
    sum_happiness = []
    for combination in (set(all_permutations)):
        temp_happiness = []
        for idx, person in enumerate(combination):
            if idx == (len(combination) - 1):
                r_neighbour = combination[0]
            else:
                r_neighbour = combination[idx + 1]
            l_neighbour = combination[idx - 1]

            [x.calculate_happiness(r_neighbour, l_neighbour) for x in part1_persons if x.Name == person]
            temp_happiness.append([x.happiness for x in part1_persons if x.Name == person])
        sum_happiness.append(temp_happiness)
    part1_result = []
    for happ in sum_happiness:
        part1_result.append(sum([sum(x) for x in happ]))

    print("Part1:", max(part1_result))
    # för att få del två, kör först utan part2 som flagga och sedan med och subtrahera resultatet..


if __name__ == '__main__':
    main()
