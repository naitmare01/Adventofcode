#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
from copy import deepcopy
import time
# import regex
from collections import defaultdict


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class AllergenAssessment():
    def __init__(self):
        self.reset()

        self.all_ingredients_cnt = defaultdict(int)
        self.allergens = defaultdict(list)
        self.all_possible = set()
        self.intersects = {}
        self.num_safe_ingredients = 0

    def reset(self):
        self.instructions = None
        self.recipes = []
        self.possible_allers = defaultdict(set)
        self.recipes_with = defaultdict(list)
        self.safe = []
        # self.num_safe_ingredients = 0
        self.exact_allers = defaultdict(set)

    def check_recipies(self):
        for line in self.instructions:
            ingredients = []

            if line[-1] == ')':
                toks = line.split(' (')
                ingredients = toks[0].split(' ')
                al = toks[1][9:-1].split(', ')
                for a in al:
                    self.allergens[a].append(set(toks[0].split(' ')))
            else:
                ingredients = line.split(' ')

            for i in ingredients:
                self.all_ingredients_cnt[i] += 1

        for k, v in self.allergens.items():
            self.intersects[k] = set.intersection(*v)
            self.all_possible.update(self.intersects[k])

        for k, v in self.all_ingredients_cnt.items():
            if k not in self.all_possible:
                self.num_safe_ingredients += 1

    def build_recipies(self):
        # self.instructions = [x.replace(')', '').split('(') for x in self.instructions]
        for idx, line in enumerate(self.instructions):
            ingredients, allergens = line.rstrip(')\n').split(' (contains ')
            ingredients = set(ingredients.split())
            allergens = set(allergens.split(', '))

            self.recipes.append(ingredients)

            for aller in allergens:
                self.recipes_with[aller].append(idx)

            for ingr in ingredients:
                self.possible_allers[ingr] |= allergens

    def safe_ingredients(self):
        for k, v in self.possible_allers.items():
            possible = deepcopy(self.possible_allers[k])
            impossible = set()
            for aller in v:
                if any(k not in self.recipes[x] for x in self.recipes_with[aller]):
                    impossible.add(aller)

            possible -= impossible
            if not possible:
                self.safe.append(k)

        # self.exact_allers = deepcopy(self.possible_allers)
        for safes in self.safe:
            # del self.exact_allers[safes]
            self.num_safe_ingredients += (sum(safes in x for x in self.recipes))

    def find_exact_ingredient(self):
        self.exact_allers = sorted(self.possible_allers, key=lambda x: len(self.possible_allers[x]))
        solution = []
        while (len(self.exact_allers) > 0):
            allergen = self.exact_allers[0]
            ing = self.possible_allers[allergen].pop()
            solution.append((self.exact_allers[0], ing))
            # delete ingredient from all allergens
            for v in self.possible_allers.values():
                if ing in v:
                    v.remove(ing)
            del self.possible_allers[allergen]
            self.exact_allers = sorted(self.possible_allers, key=lambda x: len(self.possible_allers[x]))
        print(solution)


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()

    allergens = AllergenAssessment()
    allergens.instructions = input_file
    allergens.check_recipies()
    print(f'Part1: {allergens.num_safe_ingredients}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
