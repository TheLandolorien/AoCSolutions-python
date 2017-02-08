#!C:\python27
#--- Day 19: Medicine for Rudolph ---
#http://adventofcode.com/day/19

import re, numpy as np

# Insert Methods Here


def parse_data(data):
    m = data[len(data) - 1]
    r_dict = {}
    for e in data[:len(data) - 2]:
        f, r = e.split(' => ')
        if f in r_dict:
            r_dict[f].append(r)
        else:
            r_dict[f] = [r]
    return m, r_dict

with open('input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
   

medicine_molecule, replacements = parse_data(data)

# Part 1
molecules = []
for step in medicine_molecule:
    if step in replacements:
        indices = [i for i, x in enumerate(medicine_molecule) if x == step]
        for i in indices:
            for r in replacements[step]:
                molecule = medicine_molecule[0:i] + r + medicine_molecule[i + len(step) - 1:]
                if molecule not in molecules:
                    molecules.append(molecule)

print 'There are {} distinct molecules.'.format(len(molecules))

# Part 2

