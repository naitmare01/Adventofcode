#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import re


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


def test_abba(x):
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))


def get_abas(word):
    abas = []
    for i in range(0, len(word) - 2):
        slc = word[i: i + 3]
        if slc[0] == slc[2] and slc[0] != slc[1]:
            abas.append(slc)
    return abas


def support_ssl(addr):
    regex = re.compile(r'.*\[([a-z]+)\].*')
    hypernets = []
    while True:
        m = regex.match(addr)
        if not m:
            break
        inner = m.groups()[0]
        hypernets.append(inner)
        addr = addr.replace(inner, '')
    abas = get_abas(addr)
    for a in abas:
        bab = ''.join([a[1], a[0], a[1]])
        for h in hypernets:
            if bab in h:
                return True
    return False


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
        input_file = input_file.splitlines()
    part2 = []
    for line in input_file:
        part2.append(support_ssl(line))
    input_file = [re.split(r'\[([^\]]+)\]', line) for line in input_file]
    parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in input_file]
    part1 = sum(test_abba(sn) and not(test_abba(hn)) for sn, hn in parts)
    print("Part1:", part1)
    print("Part2:", len([x for x in part2 if x is True]))


if __name__ == '__main__':
    main()
