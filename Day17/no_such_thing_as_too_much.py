#!C:\python27
#--- Day 17: No Such Thing as Too Much ---
#http://adventofcode.com/day/17

from itertools import combinations

with open('input.txt', 'r') as f:
    data = [int(line.strip()) for line in f.readlines()]

capacity = 150
solutions = []

# Part 1
for i in xrange(1, len(data)):    
    possibles = combinations(data, i)
    for possible in possibles:
        if sum(possible) == capacity:
            solutions.append(possible)



print len(solutions)

# Part 2
stop = len(data)
i = 1
while i < stop:   
    possibles = combinations(data, i)
    for possible in possibles:
        if sum(possible) == capacity:
            if len(solutions) == 0:
                stop = i
            solutions.append(possible)
    i += 1



print len(solutions)
