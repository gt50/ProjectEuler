__author__ = 'Shawn'

def get_triangles(max):
    largestc = max*max
    perimeters = {}
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
                    if not abc in perimeters:
                        perimeters[abc]=[]
                    if a < b:
                        pyth = (a,b,c)
                    else:
                        pyth = (b,a,c)
                    perimeters[abc].append(pyth)
    print perimeters
    print max(perimeters)
    #print max(perimeters, key=lambda key: len(set(perimeters[key])))
    for key in perimeters:
        perimeters[key] = len(set(perimeters[key]))
    print perimeters



get_triangles(100)