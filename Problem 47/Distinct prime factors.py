__author__ = 'Shawn'

import math

primelist = []
distinctprimefactors = []

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

def biggest_prime_factor(number):
    while number > primelist[-1]:
        primelist.append(pg.next())
    for prime in [y for y in primelist if y <= number][::-1]:
        if number % prime == 0:
            return prime
    return 1

def primefactors(maxnum):
    for i in xrange(4,maxnum):
        distinctprimefactors.append(biggest_prime_factor(i))

pg = prime_generator()
primelist.append(pg.next())
print biggest_prime_factor(14)
primefactors(100)
print distinctprimefactors