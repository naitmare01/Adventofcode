#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
from functools import lru_cache
# from itertools import combinations
# from copy import deepcopy
import time
import regex


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class MonsterMessages():
    def __init__(self):
        self.reset()

    def reset(self):
        self.result = None
        self.ruleset = {}
        self.instructions = None
        self.messages = None
        self.result = dict()

    def decode_rules(self):
        raw_rules, self.messages = self.instructions
        self.ruleset = dict(
            raw_rule.replace('"', "").split(": ", 1)
            for raw_rule in raw_rules
        )

    @lru_cache(maxsize=None)
    def solve(self, part):
        if part == 2:
            self.ruleset["8"] = "42 +"  # repeat pattern
            self.ruleset["11"] = "(?P<R> 42 (?&R)? 31 )"  # recursive pattern

        def expand(value):
            if not value.isdigit():
                return value
            return "(?:" + "".join(map(expand, self.ruleset[value].split())) + ")"

        r = regex.compile(expand("0"))
        self.result[part] = sum(r.fullmatch(m) is not None for m in self.messages)


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = [x.splitlines() for x in file.read().split('\n\n')]
    monster_messages = MonsterMessages()
    monster_messages.instructions = input_file
    monster_messages.decode_rules()
    monster_messages.solve(1)
    print(f'Part1: {monster_messages.result[1]}')
    monster_messages.solve(2)
    print(f'Part1: {monster_messages.result[2]}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
