#!C:\python27
#--- Day 14: Reindeer Olympics ---
#http://adventofcode.com/day/15

import sys, re

def main(data, time):
    reindeer = parse_data(data)

    standings = calculate_race(reindeer, time)
    print 'The winning reindeer traveled {} km using the old system.'.format(max(standings.values()))

    points = calculate_points(reindeer, time)
    print 'The winning reindeer scored {} points using the new system.'.format(max(points.values()))

def calculate_race(racers, limit):
    distances = {}

    for reindeer, stats in racers.items():
        cycle = sum(stats[1:])
        cycles = limit / cycle
        extra = limit % cycle

        speed, fly_time, rest_time = stats

        if extra > fly_time:
            cycles += 1
            distance = cycles * speed * fly_time
        else:
            distance = cycles * speed * fly_time + extra * speed

        distances[reindeer] = distance
    
    return distances

def calculate_points(racers, limit):
    points = {}

    for i in xrange(1, limit + 1):
        standings = calculate_race(racers, i)
        best_distance = max(standings.values())
        winners = [k for k,v in standings.items() if v == best_distance]

        for winner in winners:
            if winner not in points:
                points[winner] = 0

            points[winner] += 1
                
    return points
    

def parse_data(data):
    reindeer = {}

    for racer in data:
        words = racer.split(' ')
        name = words[0]
        speed = int(words[3])
        fly_time = int(words[6])
        rest_time = int(words[13])
        reindeer[name] = (speed, fly_time, rest_time)

    return reindeer

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Usage: <script_name>.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        main(lines, int(sys.argv[2]))

##with open('test.txt', 'r') as f:
##    data = [line.strip() for line in f.readlines()]
