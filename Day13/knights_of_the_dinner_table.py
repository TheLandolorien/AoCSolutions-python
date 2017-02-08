#!C:\python27
#--- Day 13: Knights of the Dinner Table ---
#http://adventofcode.com/day/13

import sys, re
from itertools import permutations

MAX = sys.maxint

def main(data):
    total = find_optimal_happiness(data)
    print 'The total change in happiness without you is {}'.format(total)

    total = find_optimal_happiness(data, you=True)
    print 'The total change in happiness with you is {}'.format(total)

def build_guest_list(info):
    guests = {}
    guest_list = []
    
    for line in lines:
        words = line.split(' ')
        guest = words[0]
        sign = words[2]
        quantity = int(words[3])
        attendee = words[10][:-1]
        
        if attendee not in guest_list:
            guest_list.append(attendee)
        if sign == 'lose':
            quantity *= -1
        if guest not in guests:
            guests[guest] = {attendee: quantity}
        else:
            guests[guest][attendee] = quantity

    return guests, guest_list
        
def find_optimal_happiness(data, you=False):
    guests, guest_list = build_guest_list(data)

    if you:
        name = 'Callie'

        guests[name] = {}
        for guest in guest_list:
            guests[name][guest] = 0
        guest_list.append(name)
        
        for guest in guests:
            guests[guest][name] = 0

        
    
    perm = permutations(guest_list)
    optimal = MAX * -1

    for p in perm:
        units = 0
        for i in xrange(len(p)):
            if i - 1 < 0:
                p_idx = len(p) - 1
            else:
                p_idx = i - 1

            if i + 1 == len(p):
                n_idx = 0
            else:
                n_idx = i + 1

            units += guests[p[i]][p[p_idx]]
            units += guests[p[i]][p[n_idx]]
            
        if units > optimal:
            optimal = units
    return optimal

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: knights_of_the_dinner_table.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        main(lines)
