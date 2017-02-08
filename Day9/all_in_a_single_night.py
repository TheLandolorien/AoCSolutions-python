#!C:\python27
#--- Day 9: All in a Single Night ---
#http://adventofcode.com/day/9
# Shortest Path Problem

import sys, re, numpy as np
from itertools import permutations

def main(data):
    key, graph = create_array(data)
    print 'The distance of the shortest route is {}.'.format(min(calc_distances(key, graph)))
    print 'The distance of the longest route is {}.'.format(max(calc_distances(key, graph)))

def create_array(paths):
    string = ' '.join(lines)
    string = re.sub(' to ', ' ', string)
    string = re.sub(' = ', ' ', string)
    string = re.sub(' \d+', '', string)

    num_cities = len(set(string.split(' ')))
    g = np.zeros((num_cities, num_cities), dtype = int)
    k = []

    for path in paths:
        v1, to, v2, equal, w = path.split(' ')
        w = int(w)

        if v1 not in k:
            k.append(v1)
        if v2 not in k:
            k.append(v2)

        g[k.index(v1)][k.index(v2)] = w
        g[k.index(v2)][k.index(v1)] = w

    return k, g

def calc_distances(cities, matrix):
    perms = permutations(cities)
    distances = []
    n = len(cities)

    for perm in perms:
        cost = 0
        for i in xrange(n - 1):
            cost += matrix[cities.index(perm[i])][cities.index(perm[i+1])]
        distances.append(cost)

    return distances

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: all_in_a_single_night.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        main(lines)
