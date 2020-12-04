#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import math


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class MeteorField:  # pylint: disable=too-few-public-methods
    def __init__(self, field):
        self.field = {(x, y) for y, l in enumerate(field) for x, c in enumerate(l) if c == '#'}

    def sort_field(self):
        self.field = sorted(self.field)


class MonitoringStation:  # pylint: disable=too-few-public-methods
    def __init__(self):
        self.base_camp = None
        self.visible_meteors = 0
        self.scanned_field = None  # scanned field with angles including base camp

    def find_base_camp(self, field):
        for start in field:
            cnt = len(set(angle(start, end) for end in field if start != end))
            if cnt > self.visible_meteors:
                self.visible_meteors = cnt
                self.base_camp = start

        self.scanned_field = sorted(((angle(self.base_camp, end), end) for end in field), key=lambda x: (x[0], abs(self.base_camp[0] - x[1][0]) + abs(self.base_camp[1] - x[1][1])))


class LaserCannon:  # pylint: disable=too-few-public-methods
    def __init__(self):
        self.name = None
        self.targeting_map = None
        self.vaporized_asteroids = []
        self.bet = None
        self.bet_asteroid = None

    def load_map(self, targeting_map):
        targeting_map.pop(0)  # Remove base camp from map
        self.targeting_map = targeting_map

    def vaporize_asteroid(self, targets):
        current_angle = targets[0][0]
        cnt = 0
        idx = 0

        self.vaporized_asteroids.append((cnt, targets.pop(0)))

        while targets:
            if idx >= len(targets):
                idx = 0
                current_angle = None
            if current_angle == targets[idx][0]:
                idx += 1
                continue
            last = targets.pop(idx)
            cnt = cnt + 1
            current_angle = last[0]
            self.vaporized_asteroids.append((cnt, last))

    def settle_bet(self, target_asteroid):
        result = self.vaporized_asteroids[target_asteroid - 1]
        self.bet_asteroid = result[1][1]
        result = (100 * result[1][1][0]) + result[1][1][1]
        self.bet = result


def angle(start, end):
    result = math.atan2(end[0] - start[0], start[1] - end[1]) * 180 / math.pi
    if result < 0:
        return 360 + result
    return result


def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().splitlines()
        meteor_field = MeteorField(input_file)

    # ##Part 1
    monitoring_station = MonitoringStation()
    monitoring_station.find_base_camp(meteor_field.field)

    print("Part1 base camp:", monitoring_station.base_camp)
    print("Part1 visible meteors:", monitoring_station.visible_meteors)

    # ##Part 2
    laser_cannon = LaserCannon()
    laser_cannon.load_map(monitoring_station.scanned_field)
    laser_cannon.vaporize_asteroid(laser_cannon.targeting_map)
    laser_cannon.settle_bet(200)
    print("Part2 elf bet:", laser_cannon.bet_asteroid)
    print("Part2 puzzle result:", laser_cannon.bet)


if __name__ == '__main__':
    main()
