#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse

def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args

def represents_int(string_to_test):
    try:
        int(string_to_test)
        return True
    except ValueError:
        return False

class Duet: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    '''
        snd X plays a sound with a frequency equal to the value of X.
        set X Y sets register X to the value of Y.
        add X Y increases register X by the value of Y.
        mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
        mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
        rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
        jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
    '''
    def __init__(self):
        self.registrer = []
        self.sound_freq = 0

    def run_instructions(self, instructions):
        idx = 0
        while True:
            instruction = instructions[idx]
            instruction = instruction.split(" ")
            operation = instruction[0]
            registrar = instruction[1]
            register_exist = [x for x in self.registrer if x[0] == registrar]

            if not register_exist:
                self.registrer.append((registrar, 0))
            index_of_registrar = [self.registrer.index(x) for x in self.registrer if x[0] == registrar][0]

            if operation == "snd":
                self.sound_freq = self.registrer[index_of_registrar][1]
            elif operation == "set":
                set_value = int(instruction[2])
                self.registrer[index_of_registrar] = (registrar, set_value)
            elif operation == "add":
                add_value = self.registrer[index_of_registrar][1] + int(instruction[2])
                self.registrer[index_of_registrar] = (registrar, add_value)
            elif operation == "mul":
                mul_value = self.registrer[index_of_registrar][1] * self.registrer[index_of_registrar][1]
                self.registrer[index_of_registrar] = (registrar, mul_value)
            elif operation == "mod":
                if represents_int(instruction[2]):
                    mod_value = self.registrer[index_of_registrar][1] % int(instruction[2])
                else:
                    index_of_registrar_instruction = [self.registrer.index(x) for x in self.registrer if x[0] == instruction[2]][0]
                    print(self.registrer[index_of_registrar][1], self.registrer[index_of_registrar_instruction][1], self.registrer)
                mod_value = self.registrer[index_of_registrar][1] % self.registrer[index_of_registrar_instruction][1]
                self.registrer[index_of_registrar] = (registrar, mod_value)
            elif operation == "rcv":
                if self.registrer[index_of_registrar][1] != 0:
                    print("exit loop")
                    break
            elif operation == "jgz":
                if self.registrer[index_of_registrar][1] > 0:
                    idx = idx + int(instruction[2])
                    continue
            idx = idx + 1

def main():
    args = arguments()

    with open(args.file) as file:
        input_file = file.read().strip().split("\n")

    duet = Duet()
    duet.run_instructions(input_file)
    print(duet.registrer, duet.sound_freq)


if __name__ == '__main__':
    main()
