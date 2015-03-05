__author__ = 'Shawn'
import math

def ispandigital(number):
    return sorted(map(int, str(number))) == range(1,len(str(number))+1) #list(set(map(int, str(number))))

def getmultiples(maxdigits):
    max_operand = (maxdigits/2)
    pandigital_multiples = []
    for i in range(1,int(math.pow(10,max_operand))):
        multiples =''
        for j in range(1,10):
            multiples = multiples + str(i*j)
            if len(multiples) > 9:
                break
            if len(multiples) == 9 and ispandigital(multiples):
                pandigital_multiples.append(int(multiples))
    print pandigital_multiples
    print list(set(pandigital_multiples))
    print max(list(set(pandigital_multiples)))

def test():
    assert ispandigital(15234) == True
    assert ispandigital(391867254) == True
    assert ispandigital(1111) == False
    print "Tests Passed!"

getmultiples(9)