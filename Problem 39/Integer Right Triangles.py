__author__ = 'Shawn'
import math

def get_triangles(maximum):
    largestc = maximum*maximum
    perimeters = {}
    for a in range (1,maximum+1):
        for b in range (1,maximum+1):
            ab = a*a + b*b
            if ab > largestc:
                break
            c = math.sqrt(ab)
            if math.floor(c) == c:
                c = int(c)
                abc = a+b+c
                if abc < maximum:
                    if not abc in perimeters:
                        perimeters[abc] = []
                    if a < b:
                        pyth = (a, b, c)
                    else:
                        pyth = (b, a, c)
                    perimeters[abc].append(pyth)
    print perimeters
    for key in perimeters:
        perimeters[key] = len(set(perimeters[key]))
    print perimeters
    print max(perimeters.values())
    most_triangles = max(perimeters.values())
    for k, v in perimeters.items():
        if v == most_triangles:
            print k



get_triangles(1000)


"""
            for c in range(1,max+1):
                cc = c*c
                if cc > ab:
                    break
                abc = a+b+c
                if ab == cc and abc < max:
                    if not abc in perimeters:
                        perimeters[abc]=[]
                    if a < b:
                        pyth = (a,b,c)
                    else:
                        pyth = (b,a,c)
                    perimeters[abc].append(pyth)
"""