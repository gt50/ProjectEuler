__author__ = 'Shawn'
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import itertools


def getpermutation(n, *digits):
    try:
        return sorted(list(itertools.permutations(digits)))[n-1]
    except:
        return None

def test():
    assert getpermutation(3,0,1,2) == (1,0,2)
    print "Tests Pass"


#print getpermutation(10,0,1,2,3,4,5,6,7,8,9)
test()

print getpermutation(1000000,0,1,2,3,4,5,6,7,8,9)
