__author__ = 'Shawn'
import math

def ispandigital(number):
    return sorted(map(int, str(number))) == range(1,len(str(number))+1) #list(set(map(int, str(number))))

def getproducts(maxdigits):
    max_operand = (maxdigits -1)/2
    pandigital_products = []
    for i in range(1,int(math.pow(10,max_operand))):
        for j in range(1,int(math.pow(10,max_operand))):
            product_length = len(str(i)+str(j)+str(i*j))
            if product_length > maxdigits:
                break
            if product_length == maxdigits:
                if ispandigital(str(i) + str(j) + str(i*j)):
                    pandigital_products.append(i*j)
    print pandigital_products
    print list(set(pandigital_products))
    print sum(list(set(pandigital_products)))

def test():
    assert ispandigital(15234) == True
    assert ispandigital(391867254) == True
    assert ispandigital(1111) == False
    print "Tests Passed!"


test()
getproducts(9)