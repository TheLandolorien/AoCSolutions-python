#!C:\python27
#--- Day 16: Aunt Sue ---
#http://adventofcode.com/day/16

import re

def parse_data(data):
    aunts = {}
    pattern = re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

    for aunt in data:
        match = re.search(pattern, aunt)
        index = int(match.group(1))
        component_key_1 = match.group(2)
        component_value_1 = int(match.group(3))
        component_key_2 = match.group(4)
        component_value_2 = int(match.group(5))
        component_key_3 = match.group(6)
        component_value_3 = int(match.group(7))

        aunts[index] = {
            component_key_1: component_value_1,
            component_key_2: component_value_2,
            component_key_3: component_value_3
        }

    return aunts

with open('input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

message = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

aunts = parse_data(data)

#  Find the aunt the gave you the present using exact values
##for i in xrange(1, 501):
##    aunt = aunts[i]
##    if [message[x] for x in aunt.keys()] == [aunt[x] for x in aunt.keys()]:
##        print i
##        break

#  Find the aunt the gave you the present using range readings
for i in xrange(1, 501):
    aunt = aunts[i]

    valid = True
    for k, v in aunt.items():
        if (k == 'cats' or k == 'trees') and v <= message[k]:
            valid = False
            break
        if (k == 'pomeranians' or k == 'goldfish') and v >= message[k]:
            valid = False
            break
        if (k == 'children' or k == 'samoyeds' or k == 'akitas'  or k == 'vizslas'  or k == 'cars'  or k == 'perfumes') and v != message[k]:
            valid = False
            break
    if valid:
        print i
        break

# The answer if greater than 40
