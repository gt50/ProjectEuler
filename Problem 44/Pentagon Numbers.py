__author__ = 'Shawn'

import itertools, sys

def get_pentagon_numbers(n):
    p = []
    for i in range(1,n+1):
        p.append(i*(3*i-1)/2)
    return p

def good_number(numbers, pentagon_numbers):
    if (numbers[0] + numbers[1]) in pentagon_numbers:
        if abs(numbers[0] - numbers[1]) in pentagon_numbers:
            return True
    return False

def check_permutations(pentagon_numbers):
    D = 0
    for pair in itertools.combinations(pentagon_numbers,2):
        if good_number(pair, pentagon_numbers):
            difference = abs(pair[0] - pair[1])
            if difference < D or D == 0:
                D = difference
    return D


def test():
    assert get_pentagon_numbers(10) == [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]

test()
pentagon_numbers =  get_pentagon_numbers(3000)
print pentagon_numbers
print check_permutations(pentagon_numbers)