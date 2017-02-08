#!C:\python27
#--- Day 8: Matchsticks ---
#http://adventofcode.com/day/8

import sys, re

def main(strings):
    print 'Code - In-memory =  {}'.format(get_total_literal_string_length(strings) - get_total_memory_string_length(strings))
    print 'Encoded -  Code = {}'.format(get_total_encoded_string_length(strings[:]) - get_total_literal_string_length(strings))

def get_total_literal_string_length(strings):
    return len(''.join(strings))

def get_total_memory_string_length(strings):
    return len(eval('+'.join(strings)))

def get_total_encoded_string_length(strings):
    for s in strings:
        index = strings.index(s)
        s = re.sub('\\\\', '\\\\\\\\', s)
        s = re.sub('"', '\\"', s)
        s = '"' + s + '"'
        strings[index] = s
    return len(''.join(strings))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: matchsticks.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        main(lines)
