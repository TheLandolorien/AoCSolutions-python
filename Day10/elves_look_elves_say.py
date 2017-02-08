#!C:\python27
#--- Day 10: Elves Look, Elves Say ---
#http://adventofcode.com/day/10

import sys, re, numpy as np

def main(data, cycles):
    length = look_and_say(data, cycles)


def look_and_say(text, n):
    string = text
    for i in xrange(n):
        s = ''
        while len(string) > 0:
            search = string[0]
            pattern = re.compile('^' + search + '+')
            match = re.match(pattern, string)
            num_found = match.group().count(search)
            s += '{}{}'.format(num_found, search)

            string = string[num_found:]
        string = s
        print 'Round {}: {}'.format(i + 1, len(string))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: elves_look_elves_say.py <input> <cycles>'
    else:
        main(sys.argv[1], int(sys.argv[2]))
