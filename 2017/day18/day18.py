#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
# from functools import lru_cache
# from itertools import permutations
from copy import deepcopy
import time
# import networkx as nx
# import collections


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class VMVersionTwo():
    def __init__(self, id):
        self.reset()
        self.instructions = None
        self.id = id

    def reset(self):
        self.memory = dict()
        self.incomming_message_queue = list()
        self.outgoing_message_queue = None
        self.state = 'terminated'  # running, waiting, terminated, queue
        self.last_index = 0
        self.num_of_send_transactions = 0

    def is_digit(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def run_vm(self):
        self.memory['p'] = self.id
        self.state = 'running'
        idx = deepcopy(self.last_index)
        while True:
            cmd = self.instructions[idx]
            inst = cmd[0]
            first_registrer = cmd[1]
            jump = 1

            if first_registrer not in self.memory and first_registrer.isalpha():
                self.memory[first_registrer] = 0
            if len(cmd) > 2:
                second_registrer = cmd[2]
                if second_registrer not in self.memory and second_registrer.isalpha():
                    self.memory[second_registrer] = 0

            if inst == 'snd':
                if first_registrer.isalpha():
                    value = self.memory[first_registrer]
                else:
                    value = int(first_registrer)
                self.outgoing_message_queue.incomming_message_queue.append(value)
                self.outgoing_message_queue.state = 'queue'
                self.num_of_send_transactions += 1
            elif inst == 'rcv':
                if len(self.incomming_message_queue) == 0:
                    self.state = 'waiting'
                    self.last_index = idx
                    break
                else:
                    self.memory[first_registrer] = self.incomming_message_queue[0]
                    del self.incomming_message_queue[0]
            if inst == 'set':
                if self.is_digit(second_registrer):
                    value = int(second_registrer)
                else:
                    value = self.memory[second_registrer]
                self.memory[first_registrer] = value
            elif inst == 'add':
                if self.is_digit(second_registrer):
                    value = int(second_registrer)
                else:
                    value = self.memory[second_registrer]
                self.memory[first_registrer] += value
            elif inst == 'mul':
                if self.is_digit(second_registrer):
                    value = int(second_registrer)
                else:
                    value = self.memory[second_registrer]
                self.memory[first_registrer] *= value
            elif inst == 'mod':
                if self.is_digit(second_registrer):
                    value = int(second_registrer)
                else:
                    value = self.memory[second_registrer]
                self.memory[first_registrer] = self.memory[first_registrer] % value
            elif inst == 'jgz':
                jumping = False
                if self.is_digit(first_registrer):
                    if int(first_registrer) > 0:
                        jumping = True
                elif self.memory[first_registrer] > 0:
                    jumping = True
                if jumping:
                    if self.is_digit(second_registrer):
                        jump = int(second_registrer)
                    else:
                        jump = self.memory[second_registrer]
            idx += jump


class VM():
    def __init__(self):
        self.reset()
        self.instructions = None

    def reset(self):
        self.memory = dict()
        self.last_sound = None
        self.recoved_frequency = None

    def is_digit(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def run_vm(self):
        idx = 0
        while True:
            cmd = self.instructions[idx]
            inst = cmd[0]
            first_registrer = cmd[1]
            jump = 1

            if first_registrer not in self.memory and first_registrer.isalpha():
                self.memory[first_registrer] = 0
            if len(cmd) > 2:
                second_registrer = cmd[2]
                if second_registrer not in self.memory and second_registrer.isalpha():
                    self.memory[second_registrer] = 0

            if inst == 'set':
                if self.is_digit(second_registrer):
                    value = int(second_registrer)
                else:
                    value = self.memory[second_registrer]
                self.memory[first_registrer] = value
            elif inst == 'snd':
                self.last_sound = int(self.memory[first_registrer])
            elif inst == 'add':
                if self.is_digit(second_registrer):
                    value = int(second_registrer)
                else:
                    value = self.memory[second_registrer]
                self.memory[first_registrer] += value
            elif inst == 'mul':
                if self.is_digit(second_registrer):
                    value = int(second_registrer)
                else:
                    value = self.memory[second_registrer]
                self.memory[first_registrer] *= value
            elif inst == 'mod':
                if self.is_digit(second_registrer):
                    value = int(second_registrer)
                else:
                    value = self.memory[second_registrer]
                self.memory[first_registrer] = self.memory[first_registrer] % value
            elif inst == 'jgz':
                jumping = False
                if self.is_digit(first_registrer):
                    if int(first_registrer) > 0:
                        jumping = True
                elif self.memory[first_registrer] > 0:
                    jumping = True
                if jumping:
                    if self.is_digit(second_registrer):
                        jump = int(second_registrer)
                    else:
                        jump = self.memory[second_registrer]
            elif inst == 'rcv':
                if self.memory[first_registrer] != 0:
                    self.recoved_frequency = self.last_sound
                    break
            idx += jump


def main():
    startTime = time.time()
    args = arguments()
    with open(args.file) as file:
        input_file = file.read().splitlines()
        input_file = [x.split() for x in input_file]
    vm = VM()
    vm.instructions = input_file
    vm.run_vm()
    print(f'Part1: {vm.recoved_frequency}')
    vm_one = VMVersionTwo(0)
    vm_two = VMVersionTwo(1)
    vm_one.instructions = input_file
    vm_two.instructions = input_file
    vm_one.outgoing_message_queue = vm_two
    vm_two.outgoing_message_queue = vm_one

    vms = [vm_one, vm_two]
    running_vm_idx = 0
    while True:
        if all(x.state == 'waiting' for x in vms):
            break
        if vms[running_vm_idx].state == 'waiting':
            if running_vm_idx == 0:
                running_vm_idx = 1
            else:
                running_vm_idx = 0
        else:
            vms[running_vm_idx].run_vm()

    print(f'Part2: {vm_two.num_of_send_transactions}')
    print(f'Execution time in seconds: {(time.time() - startTime)}')


if __name__ == '__main__':
    main()
