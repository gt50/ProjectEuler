__author__ = 'Shawn'
import sys

triangle = (n*(n+1)/2 for n in xrange(1, sys.maxint))
pentagonal = (n*(3*n-1)/2 for n in xrange(1, sys.maxint))
hexagonal = (n*(2*n-1) for n in xrange(1, sys.maxint))

t = [0]
p = [0]
h = [0]

def x(generator, arr, maxnum):
    while max(arr) < maxnum:
        arr.append(next(generator))
        max(arr)

def check_triangles(maxnum):
    while max(t) < maxnum:
        t.append(next(triangle))
        x(pentagonal, p, max(t))
        x(hexagonal, h, max(t))
        if (max(t) in p) and (max(t) in h):
            print max(t)

check_triangles(10000000000)