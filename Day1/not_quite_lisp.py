#!C:\python27
#--- Day 1: Not Quite Lisp ---
#http://adventofcode.com/day/1

import sys

def main(instructions):
    location = get_floor(instructions)
    print 'Santa is located on the floor {}'.format(location)
    entrance = get_basement_entrance_index(instructions)
    print 'Santa entered the basement at {}'.format(entrance)

def get_floor(instructions):
    return instructions.count('(') - instructions.count(')')

def get_basement_entrance_index(instructions):
    location = 0

    for i in xrange(len(instructions)):
        if instructions[i] == '(':
            location += 1
        else:
            location -= 1
        if location == -1:
            return i + 1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python not_quite_lisp.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            instructions = f.readlines()
        main(instructions[0])
