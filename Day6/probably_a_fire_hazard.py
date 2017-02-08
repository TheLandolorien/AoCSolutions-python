#!C:\python27
#--- Day 6: Probably a Fire Hazard ---
#http://adventofcode.com/day/6

import sys, re
import numpy as np

pattern = re.compile(r'(t.+) (\d*,\d*) through (\d*,\d*)')

def main(instructions):
    num_on = count_on_lights(instructions)
    print '{} lights are lit.'.format(num_on)

    num_on_translated = count_on_lights_translated(instructions)
    print 'The total brightness of the lights are {}.'.format(num_on_translated)

def count_on_lights(instructions):
    lights = np.zeros((1000,1000), dtype=bool)

    for instruction in instructions:
        match = pattern.match(instruction)
        command = match.group(1)
        x1, y1 = map(int, match.group(2).split(','))
        x2, y2 = map(int, match.group(3).split(','))

        if command == 'turn on':
            lights[x1:x2+1,y1:y2+1] = True
        elif command == 'turn off':
            lights[x1:x2+1,y1:y2+1] = False
        else: # toggle
            lights[x1:x2+1,y1:y2+1] = np.invert(lights[x1:x2+1,y1:y2+1])

    return np.sum(lights)

def count_on_lights_translated(instructions):
    lights = np.zeros((1000,1000), dtype=np.int)

    for instruction in instructions:
        match = pattern.match(instruction)
        command = match.group(1)
        x1, y1 = map(int, match.group(2).split(','))
        x2, y2 = map(int, match.group(3).split(','))

        if command == 'turn on':
            lights[x1:x2+1,y1:y2+1] += 1
        elif command == 'turn off':
            lights[x1:x2+1,y1:y2+1] -= 1
            lights[lights < 0] = 0
        else: # toggle
            lights[x1:x2+1,y1:y2+1] += 2


    return np.sum(lights)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python probably_a_fire_hazard.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            instructions = [line.strip() for line in f.readlines()]
        main(instructions)
