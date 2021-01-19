#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import combinations
# from copy import deepcopy
import time
import hashlib


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Password():
    def __init__(self):
        self.reset()
        self.instructions = None
        self.encoded_password = []

    def reset(self):
        return

    def encode(self):
        idx = 0
        while len(self.encoded_password) < 6:
            result = hashlib.md5(b'{self.instructions + str(idx)}')
            if result.hexdigest().startswith('00000'):
                print(result.hexdigest())
                break
            idx += 1


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read()
    password = Password()
    password.instructions = input_file
    password.encode()
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
