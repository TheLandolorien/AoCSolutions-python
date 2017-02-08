#!C:\python27
#--- Day 18: Like a GIF For Your Yard ---
#http://adventofcode.com/day/18

import numpy as np

def parse_data(data):
    n = len(data)
    lights = np.zeros((n, n),dtype=bool)
    light_map = {'#': True, '.': False}

    for i in xrange(n):
        lights[i] = [light_map[x] for x in data[i]]

    return lights

def get_neighbors(a, i, j):
    x_start = i - 1
    y_start = j - 1
    x_stop = i + 2
    y_stop = j + 2
    
    if i == 0:
        x_start = i
    if j == 0:
        y_start = j
    if i == len(a):
        x_stop = i
    if j == len(a):
        y_stop = j
    
    return a[x_start:x_stop, y_start:y_stop]

def adv_frame_p1(lights, num_frames):
    frame_num = 1
    l = np.copy(lights)
    n = len(lights)
    
    while frame_num <= num_frames:
        next_frame = np.zeros((n, n),dtype=bool)

        for i in xrange(n):
            for j in xrange(n):
                light_neighbors = get_neighbors(l, i, j)

                on = np.count_nonzero(light_neighbors)
                if l[i][j]:
                    on -= 1
                
                if on == 3 or (l[i][j] and on == 2):
                    next_frame[i][j] = True

        l = np.copy(next_frame)
        frame_num += 1


    return l


def adv_frame_p2(lights, num_frames):
    frame_num = 1
    l = np.copy(lights)
    n = len(lights)
    
    while frame_num <= num_frames:
        next_frame = np.zeros((n, n),dtype=bool)

        l[0][0] = True
        l[n-1][n-1] = True
        l[0][n-1] = True
        l[n-1][0] = True

        for i in xrange(n):
            for j in xrange(n):
                light_neighbors = get_neighbors(l, i, j)

                on = np.count_nonzero(light_neighbors)
                if l[i][j]:
                    on -= 1
                
                if on == 3 or (l[i][j] and on == 2):
                    next_frame[i][j] = True

        next_frame[0][0] = True
        next_frame[n-1][n-1] = True
        next_frame[0][n-1] = True
        next_frame[n-1][0] = True
        
        l = np.copy(next_frame)
        frame_num += 1


    return l

rounds = 100
filename = 'input.txt'

with open(filename, 'r') as f:
    data = [line.strip() for line in f.readlines()]


lights = parse_data(data)

# Part 1
lights_p1 = adv_frame_p1(lights, rounds)
print np.count_nonzero(lights_p1)

# Part 2
lights_p2 = adv_frame_p2(lights, rounds)
print np.count_nonzero(lights_p2)

# Part 2: 1061 is too hight
