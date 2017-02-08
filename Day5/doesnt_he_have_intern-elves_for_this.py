#!C:\python27
#--- Day 5: Doesn't He Have Intern-Elves For This? ---
#http://adventofcode.com/day/5

import sys, re

banned = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
double_letter = re.compile(r'.*(.)\1.*', re.IGNORECASE)

def main(text):
    num_nice1 = count_nice1(text)
    print 'Part One: {} strings are nice.'.format(num_nice1)
    
    num_nice2 = count_nice2(text)
    print 'Part Two: {} strings are nice.'.format(num_nice2)
        
def count_nice1(str_list):
    nice_count = 0
    
    for string in str_list:
        if not has_banned(string) and has_enough_vowels(string) and has_double_letters(string):
            nice_count += 1
    return nice_count

def count_nice2(str_list):
    nice_count = 0
    
    for string in str_list:
        if has_letter_pairs(string) and has_singly_separated_letters(string):
            nice_count += 1
    return nice_count  

def has_banned(word):
    return any(x in word for x in banned)
    
def has_enough_vowels(word):
    num_vowels = 0
    for let in word:
        if let in vowels:
            num_vowels += 1
    return num_vowels >= 3

def has_double_letters(word):
    match = double_letter.match(word)
    if match:
        return True
    return False

def has_letter_pairs(word):
    for i in xrange(1, len(word)):
        pair = word[i-1:i+1]
        if word.count(pair) > 1:
            return True
    return False

def has_singly_separated_letters(word):
    for i in xrange(2, len(word)):
        let = word[i]
        if let == word[i-2]:
            return True
    return False
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python doesnt_he_have_intern-elves_for_this.py <filename>'
    else:
        with open(sys.argv[1], 'r') as f:
            strings = [line.strip() for line in f.readlines()]
        main(strings)
