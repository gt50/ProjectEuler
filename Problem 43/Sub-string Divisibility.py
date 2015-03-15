__author__ = 'Shawn'

import itertools

def is_substring_divisible(number):
    primes = [2,3,5,7,11,13,17]
    number = str(number)
    for i in range(len(primes)):
        x = int(number[1+i:4+i])
        if x % primes[i] != 0:
            return False
        #print x, i, primes[i]
    return True

def get_pandigitals():
    x = '0123456789'
    a = list(itertools.permutations(x,10))
    pandigitals = []
    for j in a:
        k = int(''.join(j))
        if is_substring_divisible(k):
            pandigitals.append(k)
    print pandigitals, len(pandigitals), sum(pandigitals)

get_pandigitals()
#print is_substring_divisible(1406357289)
