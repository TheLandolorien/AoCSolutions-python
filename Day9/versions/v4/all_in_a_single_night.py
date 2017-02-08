#!C:\python27
#--- Day 9: All in a Single Night ---
#http://adventofcode.com/day/9
# Shortest Path Problem

import sys, re
from prim_tree import Graph, Tree, Vertex

INFINITY = sys.maxint

def main(data):
    prim(data)

def prim(paths):
    t = Tree('Route')
    g = Graph('Deliveries')
    q = {}

    # Initialize Graph
    for path in paths:
        v1_name, to, v2_name, equal, w = path.split(' ')
        w = int(w)

        v1 = g.find(v1_name)
        if not v1:
            v1 = Vertex(v1_name)
            g.add_vertex(v1)
        v2 = g.find(v2_name)
        if not v2:
            v2 = Vertex(v2_name)
            g.add_vertex(v2)
        g.vertices[v1_name][1][v2_name] = w
        g.vertices[v2_name][1][v1_name] = w

    

    # Initialize Tree
    for v in g.vertices:
        q[len(q)] = [v, INFINITY, False]
        
    # Pick starting vertex
    current_index = 0

    current = q[current_index]
    v1 = g.find(current[0])

    current[1] = 0
    current[2] = True
    t.add_vertex(v1)
    
    
    possibles = [q[x][0] for x in q if not q[x][2]]

    while len(possibles) > 0 and current_index < len(q):
        try:
            shortest = min({k:v for k, v in g.vertices[current[0]][1].items() if k in possibles}.items(), key=lambda x: x[1])
        except ValueError:
            current_index += 1
        for index, vertex in q.items():
            if vertex[0] == shortest[0]:
                cost = shortest[1]
                vertex[1] = cost
                vertex[2] = True
                v2 = g.find(vertex[0])
                t.add_vertex(v2)
                t.add_edge(v1, v2, cost)
                break
        possibles = [q[x][0] for x in q if not q[x][2]]
        current = q[current_index]
        v1 = g.find(current[0])

    print t

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: all_in_a_single_night.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        main(lines)
