#!C:\python27
#--- Day 11: Corporate Policy ---
#http://adventofcode.com/day/11

import sys, re, math
from string import ascii_lowercase
from itertools import product, islice

banned = ['i', 'o', 'l']
double_letter = re.compile(r'.*(.){1}.*(.){1}.*', re.IGNORECASE)
MAX = sys.maxint
used = ['vzbxxyzz']

def main(string):
    next_password = generate_password(string)
    print 'Santa\'s next password should be {}.'.format(next_password)

def valid_password(s):
    return not has_banned(s) and has_double_letters(s) and has_straight(s) and s not in used

def has_banned(word):
    return any(x in word for x in banned)

def has_double_letters(word):
    match = re.match(double_letter, word)
    if match and match.group(1) != match.group(2):
        return True
    return False

def has_straight(word):
    for i in xrange(1, len(word) - 1):
        if ord(word[i-1]) == ord(word[i]) - 1 == ord(word[i+1]) - 2:
            return True
    return False

def generate_password(s):
    passwords = product(ascii_lowercase, repeat=8)
    password = ''.join(passwords.next())

    print 'Search for starting point {}...'.format(s)
    # Skip forward to passwords starting with the same letter
    consume(passwords, (ord(s[0]) - 97) * int(math.pow(26, 7)))

    print 'Now working on passwords starting with {}'.format(password[0])
    
    while True:
        if valid_password(password):
            return password
        try:
            password = ''.join(passwords.next())
        except StopIteration:
            print 'Next password not found!'
            raise

def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        while n > MAX:
            next(islice(iterator, MAX, MAX), None)
            n -= MAX
        next(islice(iterator, n, n), None)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: corporate_policy.py <input>'
    else:
        main(sys.argv[1])
