__author__ = 'Shawn'

import math


def is_prime(number):
    s = int(math.sqrt(number) + 1)
    if number < 2:
        return False
    for i in range(2, s):
        if number % i == 0:
            return False
    return True

def find_primes(max):
    primes = []
    for i in range(max):
        if is_prime(i):
            primes.append(i)
    return primes

def is_circular_prime(number):
    for i in range(1,len(str(number))):
        j = int(str(number)[i:] + str(number)[:i])
        if not is_prime(j):
            return False
    return True

def find_circular_primes(max):
    circular_primes = []
    for i in range(max):
        if is_prime(i):
            if is_circular_prime(i):
                circular_primes.append(i)
    return circular_primes


def test():
    assert is_prime(7) == True
    assert is_prime(100) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert find_primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert is_circular_prime(197) == True
    assert is_circular_prime(100) == False
    assert find_circular_primes(100) == [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
    print "Tests Passed"

test()

print len(find_circular_primes(1000000))