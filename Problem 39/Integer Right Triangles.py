__author__ = 'Shawn'

def get_triangles(max):
    largestc = max*max

    for a in range (1,max+1):
        for b in range (1,max+1):
            ab = a*a + b*b
            if ab > largestc:
                break
            for c in range(1,max+1):
                cc = c*c
                if cc > ab:
                    break
                abc = a+b+c
                if ab == cc and abc < max:
                    if a < b:
                        print a, b, c, abc
                    else:
                        print b, a, c, abc

get_triangles(1000)