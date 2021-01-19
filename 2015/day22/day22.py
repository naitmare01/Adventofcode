#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import random


def arguments():
    # Handle command line arguments
    parser = argparse.ArgumentParser(description='Adventofcode.')
    parser.add_argument('-f', '--file', required=True)

    args = parser.parse_args()

    return args


class Player():
    def __init__(self):
        self.reset()

    def reset(self):
        self.hp = 50
        self.armor = 0
        self.mana = 500
        self.effects = None
        self.avalible_spells = dict()

    def learn_spells(self):
        # name, manacost, damage, healing, effect
        spells = [('MM', 53, 4, None, None), ('DRAIN', 73, 2, 2, None), ('SHIELD', 113, None, None, True), ('POISON', 173, 3, None, True), ('RECHARGE', 229, None, None, True)]
        for s in spells:
            self.avalible_spells[s[0]] = Spell(s[0], s[1], s[2], s[3], s[4])
            if self.avalible_spells[s[0]].effect:
                if s[0] == 'SHIELD':
                    self.avalible_spells[s[0]].type_of_effect = {'armor': 7}
                    self.avalible_spells[s[0]].len_of_effect = 6
                if s[0] == 'POISON':
                    self.avalible_spells[s[0]].type_of_effect = {'damage': 3}
                    self.avalible_spells[s[0]].len_of_effect = 6
                if s[0] == 'RECHARGE':
                    self.avalible_spells[s[0]].type_of_effect = {'mana': 101}
                    self.avalible_spells[s[0]].len_of_effect = 5

    def select_random_spell(self):
        return (random.choice(list(self.avalible_spells.items())))

    def attack(self, opponent):
        spell = self.select_random_spell()
        spell_dmg = (self.avalible_spells[spell[0]].damage)
        if spell_dmg:
            return spell_dmg


class Boss():
    def __init__(self):
        self.reset()

    def reset(self):
        self.hp = None
        self.damage = None
        self.effects = None

    def attack(self, opponent):
        dealt_dmg = self.damage - opponent.armor
        if dealt_dmg <= 0:
            dealt_dmg = 1
        return dealt_dmg


class Spell():
    def __init__(self, name, mana_cost, damage, healing, effect):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.healing = healing
        self.effect = effect
        self.type_of_effect = None
        self.len_of_effect = None


def main():
    args = arguments()
    with open(args.file) as file:
        input_file = [line.strip() for line in file.readlines()]
        input_file = [x.split(': ') for x in input_file]

    boss = Boss()
    boss.hp = int(input_file[0][1])
    boss.damage = int(input_file[1][1])
    player = Player()
    player.learn_spells()
    while True:
        # Player turn
        dmg = player.attack(boss)
        if dmg:
            boss.hp -= dmg
        if boss.hp <= 0:
            print("Boss dies")
            break

        # boss turn
        player.hp -= boss.attack(player)
        if player.hp <= 0:
            print("player dies")
            break
    print("Boss", boss.__dict__)
    print("Player", player.__dict__)


if __name__ == '__main__':
    main()

# Återstår att bygga olika condition för vad spellen kan göra. Samt att itertera figthen
# X antal gånger och hålla koll på minst mängd mana spenderad.
