#!C:\python27
#--- Day 4: The Ideal Stocking Stuffer ---
#http://adventofcode.com/day/4

import sys, hashlib

def main(key):
    answer, md5hash = find_partial_md5_hash(key)
    print 'The answer is {}, because the MD5 hash of {}{} starts with five zeroes ({}).'.format(answer, key, answer, md5hash)
        
def find_partial_md5_hash(key):
    i = 1

    while True:
        md5hash = hashlib.md5(key+str(i)).hexdigest()
        if md5hash.startswith('000000'):
            return i, md5hash
        i += 1
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python the_ideal_stocking_stuffer.py <key>'
    else:
        main(sys.argv[1])
