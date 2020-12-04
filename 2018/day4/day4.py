#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import datetime
from collections import Counter

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

class Guard: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    guards_dict = {}

    def __init__(self, name):
        self.name = name
        self.sleep_schedule = []
        self.time_asleep = 0
        Guard.guards_dict[name] = self
        self.minutes_asleep = []
        self.most_minutes_asleep = None
        self.most_common_minute_sleeping = None
        self.part1_result = None
        self.part2_result = None

    def log_sleep_schedule(self, schedule):
        self.sleep_schedule.append(schedule)

    def calculate_sleep(self):
        datetime_format = '%H:%M'
        last_falling_asleep = None
        for minutes in self.sleep_schedule:
            if "falls asleep" in minutes:
                last_falling_asleep = minutes[12:17]
            elif "wakes up" in minutes:
                time_sleeping = datetime.datetime.strptime(minutes[12:17], datetime_format) - datetime.datetime.strptime(last_falling_asleep, datetime_format)
                self.time_asleep = self.time_asleep + time_sleeping.seconds

                sleep_dt = datetime.datetime.strptime(last_falling_asleep, datetime_format)
                wake_dt = datetime.datetime.strptime(minutes[12:17], datetime_format)
                for specific_minute in range(sleep_dt.minute, wake_dt.minute):
                    self.minutes_asleep.append(specific_minute)
        if self.minutes_asleep == []:
            self.minutes_asleep = [0, 0]

        self.minutes_asleep = Counter(self.minutes_asleep)
        self.most_minutes_asleep = self.minutes_asleep.most_common()[0][0]
        self.most_common_minute_sleeping = self.minutes_asleep.most_common()[0]

    def calculate_part1_result(self):
        self.part1_result = int(self.name[1:]) * self.most_minutes_asleep

    def calculate_part2_result(self):
        self.part2_result = int(self.name[1:]) * self.most_common_minute_sleeping[0]

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().splitlines()
    sorted_schedule = (sorted(input_file))

    #part1
    guards = []
    guard_id = -1
    for row in sorted_schedule:
        if row.split()[3] in Guard.guards_dict:
            guard = Guard.guards_dict[row.split()[3]]
            guard.log_sleep_schedule(row)
        else:
            if guard_id != row.split()[3]:
                if "Guard" in row:
                    guard_id = row.split()[3]
                    guard = Guard(guard_id)
                    guards.append(guard)
                else:
                    guard.log_sleep_schedule(row)

    time_asleep = -1
    times_asleep_per_minute = -1
    for row in guards:
        row.calculate_sleep()
        #part1
        if row.time_asleep > time_asleep:
            time_asleep = row.time_asleep
            most_sleepy_guard = row
        #part2
        if row.most_common_minute_sleeping[1] > times_asleep_per_minute:
            times_asleep_per_minute = row.most_common_minute_sleeping[1]
            most_sleepy_guard_part2 = row

    most_sleepy_guard.calculate_part1_result()
    most_sleepy_guard_part2.calculate_part2_result()

    print("part1 result:", most_sleepy_guard.part1_result)
    print("part2 result:", most_sleepy_guard_part2.part2_result)

if __name__ == '__main__':
    main()
