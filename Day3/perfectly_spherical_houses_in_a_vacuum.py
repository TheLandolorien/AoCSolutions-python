#!C:\python27
#--- Day 3: Perfectly Spherical Houses in a Vacuum ---
#http://adventofcode.com/day/3

import sys

def main(instructions):
    manual_visited_houses = find_recieving_houses_manual(instructions)
    print 'Santa visited {} houses.'.format(len(manual_visited_houses))

    automated_visited_houses = find_recieving_houses_automated(instructions)
    print 'Santa and Robo-Santa visited {} houses.'.format(len(automated_visited_houses))
    
def find_recieving_houses_manual(instructions):
    visited = {}
    location = [0,0]

    for move in instructions:
        location = update_location(move, location)
        visited = update_deliveries(tuple(location), visited)
    return visited

def find_recieving_houses_automated(instructions):
    visited = {}
    santa_location = [0,0]
    robot_location = [0,0]

    for i in xrange(1, len(instructions), 2):
        santa_move = instructions[i-1]
        robot_move = instructions[i]
        
        santa_location = update_location(santa_move, santa_location)
        robot_location = update_location(robot_move, robot_location)
        
        visited = update_deliveries(tuple(santa_location), visited)
        visited = update_deliveries(tuple(robot_location), visited)

    return visited

def update_location(move, location):
    if move == '^':
        location[1] += 1
    elif move == 'v':
        location[1] -= 1
    elif move == '>':
        location[0] += 1
    else: # location == '>'
        location[0] -= 1
    return location

def update_deliveries(coordinate, visited):
    if coordinate not in visited:
        visited[coordinate] = 1
    else:
        visited[coordinate] += 1
    return visited

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python perfectly_spherical_houses_in_a_vacuum.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            instructions = f.readlines()
        main(instructions[0])
