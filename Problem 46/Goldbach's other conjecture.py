__author__ = 'Shawn'
import sys
import math


twoxsquares_generator = (2*x*x for x in xrange(1,sys.maxint))
primelist = []
squarelistx2 = []


def prime_generator():
    primelist = []

    def is_prime(number):
        s = int(math.sqrt(number) + 1)
        if number < 2:
            return False
        if number == 2:
            return True
        for i in [prime for prime in primelist if prime <= s]:
            if number % i == 0:
                return False
        return True

    if primelist == []:
        primelist.append(2)
        yield 2
    x = 3
    while True:
        if is_prime(x):
            primelist.append(x)
            yield x
        x += 2

def is_sumprime_twicesquare(number):
    while number > max(primelist):
        primelist.append(pg.next())
    while number > max(squarelistx2):
        squarelistx2.append(next(twoxsquares_generator))
    for prime in [y for y in primelist if y < number]:
        if (number - prime) in squarelistx2:
            return True
    return False

def smallest_odd_composite(maxnumber):
    i = 7
    while i < maxnumber:
        i += 2
        if is_sumprime_twicesquare(i) or i in primelist:
            continue
        else:
            print i
            break



pg = prime_generator()
primelist.append(pg.next())
squarelistx2.append(next(twoxsquares_generator))
smallest_odd_composite(100000)
