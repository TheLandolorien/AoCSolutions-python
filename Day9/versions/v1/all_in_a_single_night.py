#!C:\python27
#--- Day 9: All in a Single Night ---
#http://adventofcode.com/day/9
# Shortest Path Problem

import sys, re, random
from prim_tree import Tree, Vertex

def main(data):
    deliveries = create_tree(data)
    path, distance = prim(deliveries)

def create_tree(commands):
    t = Tree('Deliveries')

    for command in commands:
        v1_name, to, v2_name, equal, w = command.split(' ')
        w = int(w)

        v1 = t.find(v1_name)
        if not v1:
            v1 = Vertex(v1_name)
            if len(t.vertices) == 0:
                t.set_root(v1)
            else:
                t.add_vertex(v1)

        v2 = t.find(v2_name)
        if not v2:
            v2 = Vertex(v2_name)

        v1.add_sibling(v2, w)
        

    return t

def prim(g):
    p = g
    best_path = []
    total_distance = 0
    
    # Step 1: Arbitrarily choose starting Vertex
    root = p.vertices[random.choice(p.vertices.keys())]
    best_path.append(root.name)

    while len(p.edges) > 0: # Step 3: Repeat until all Edges + Vertices added

        # Step 2: Find smallest adjacent edge + neighbor and add to path
        smallest_path = min(root.siblings.items(), key=lambda x: x[1])
        best_path.append(smallest_path[0])
        total_distance += smallest_path[1]

        root = p.find(smallest_path[0])

    return best_path, total_distance

if __name__ == '__main__':
##    if len(sys.argv) != 2:
##        print 'Usage: all_in_a_single_night.py <filename>'
##    else:
##        with open(sys.argv[1], 'r') as f:
        with open('test.txt', 'r') as f:
            lines = [line.strip() for line in f.readlines()]
##        main(lines)
