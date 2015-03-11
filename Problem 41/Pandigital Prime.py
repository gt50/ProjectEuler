__author__ = 'Shawn'

import math
import itertools


def ispandigital(number):
    return sorted(map(int, str(number))) == range(1,len(str(number))+1)


def is_prime(number, primes):
    s = int(math.sqrt(number) + 1)
    if number < 2:
        return False
    for i in primes:
        if number % i == 0:
            return False
        elif i > s:
            break
    return True

def generate_primes(maxnumber):
    a = []
    primes = [2]
    for i in range(3,maxnumber + 1):
        s = int(math.sqrt(i) + 1)
        isprime = True
        for j in primes:
            m = max(primes)
            if i % j == 0:
                isprime = False
                break
            elif j > s:
                break
        if isprime:
            #print i
            primes.append(i)
    print primes
    return primes


def get_pandigitals(maxdigits):
    x = ''
    for i in range(1,maxdigits+1):
        x += str(i)
        a = list(itertools.permutations(x,i))
        for j in a:
            k = int(''.join(j))
            if is_prime(k,primelist):
                print k

def test():
    assert is_prime(7, primelist) == True
    assert is_prime(100, primelist) == False
    assert is_prime(17, primelist) == True
    assert is_prime(1, primelist) == False
    print "Tests Passed!!!"

primelist = generate_primes(32000)
test()
get_pandigitals(9)
