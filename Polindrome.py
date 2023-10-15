# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 09:53:28 2023

@author: User
"""

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def closest_higher(target, collection) :
    """Return the closest number to `target` in `collection`
    that is higher than `target`"""
    return max((target - i, i) for i in collection if (target - i) < 0)[1]

def closest_lower(target, collection) :
    """Return the closest number to `target` in `collection`
    that is lower than `target`"""
    return min((target - i, i) for i in collection if (target - i) > 0)[1]

class Range(object):
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.palindromes = []

def main():
    ranges = [Range(*[int(i) for i in line.split()]) for line in open('seed.txt')]
    for r in ranges:
        lo, hi = r.lo, r.hi
        for p in [ran for ran in ranges if ran != r and ran.palindromes]:
            # r fits within the range of p, take all p's palindromes
            if p.lo <= r.lo <= p.hi and p.lo <= r.hi <= p.hi:
                x = p.palindromes.index(closest_higher(r.lo, p.palindromes))
                y = p.palindromes.index(closest_higher(r.hi, p.palindromes))
                r.palindromes = p.palindromes[x:y]
                lo, hi = 1, 0
                break
            # r's higher bound is within p's range, take p's palindromes
            # from p.lo to r.hi and calculate the rest of r's palindromes
            elif r.lo <= p.lo and p.lo <= r.hi <= p.hi:
                y = p.palindromes.index(closest_higher(r.hi, p.palindromes))
                hi = p.lo
                r.palindromes = p.palindromes[:y]
                break
            # r's lower bound is within p's range, take p's palindromes
            # from r.lo to p.hi and calculate the rest of r's palindromes
            elif p.lo <= r.lo <= p.hi and r.hi >= p.hi:
                x = p.palindromes.index(closest_higher(r.lo, p.palindromes))
                lo = p.hi
                r.palindromes = p.palindromes[x:]
                break
        while hi >= lo:
            if is_palindrome(lo):
                r.palindromes.append(lo)
            lo += 1
        r.palindromes = sorted(r.palindromes)

    total = 0
    for r in ranges:
        c = len(r.palindromes)
        total += c
        print ('%6d => %7d : %d' % (r.lo, r.hi, c))
    print ('TOTAL: %d' % total)

if  __name__ =='__main__':
    main()