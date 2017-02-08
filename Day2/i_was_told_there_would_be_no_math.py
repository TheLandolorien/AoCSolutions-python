
#!C:\python27
#--- Day 2: I Was Told There Would Be No Math ---
#http://adventofcode.com/day/2

import sys

def main(dimensions):
    paper_amount = calculate_needed_paper(dimensions)
    print 'The elves need {} sqft. of wrapping paper.'.format(paper_amount)

    ribbon_amount = calculate_needed_ribbon(dimensions)
    print 'The elves need {} sqft. of ribbon.'.format(ribbon_amount)

def calculate_needed_ribbon(dimensions):
    total = 0

    for dimension in dimensions:
        l, w, h = map(int, dimension)        
        total += min(2*l+2*w, 2*w+2*h, 2*h+2*l) + l*w*h
    return total

def calculate_needed_paper(dimensions):
    total = 0

    for dimension in dimensions:
        l, w, h = map(int, dimension)        
        total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    return total

def format_dimensions(dimensions_list):
    return [dimension.split('x') for dimension in dimensions_list]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python i_was_told_there_would_be_no_math.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            dimensions_list = [line.strip() for line in f.readlines()]
        main(format_dimensions(dimensions_list))
