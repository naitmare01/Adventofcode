#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import socket
import struct
from functools import lru_cache


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class StringToIP():
    def __init__(self):
        self.reset()

    def reset(self):
        self.strings = None
        self.ips = []

    @lru_cache(maxsize=None)
    def convert_string_to_ip(self):
        for row in self.strings:
            for n in range(int(row[0]), int(row[1]) + 1):
                self.ips.append(socket.inet_ntoa(struct.pack('>L', n)))

    @lru_cache(maxsize=None)
    def convert_ip_to_string(self, ip):
        return struct.unpack('>L', socket.inet_aton(ip))[0]


def main():
    args = arguments()
    with open(args.file) as file:
        record = []
        for line in file:
            a, b = [int(i) for i in line.strip().split("-")]
            record.append((a, b))

    record.sort()
    total, ip, index = 0, 0, 0
    while ip < 2**32:
        lower, upper = record[index]
        if ip >= lower:
            if ip <= upper:
                ip = upper + 1
                continue
            index += 1
        else:
            total += 1
            ip += 1

    print(total, ip, index)


if __name__ == '__main__':
    main()
